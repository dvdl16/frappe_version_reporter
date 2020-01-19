import frappe
from subprocess import check_output
from subprocess import call
import os.path
import re
from distutils.version import StrictVersion
import urllib.request
from urllib.error import HTTPError



@frappe.whitelist()
def get_frappe_app_versions(format='prtg'):
    # Get path to Frappe Bench
    bench_path = "~/frappe-bench"
    full_bench_path = os.path.expanduser(bench_path)

    # Run the "bench version" command in the correct dir, and capture the output
    out = check_output(["bench", "version"], cwd=full_bench_path)

    # Parse the output and build a list of dicts
    list = out.decode("utf-8").splitlines()
    app_list = []
    for line in list:
        app = {}
        split_line = line.split()
        app['name'] = split_line[0]
        app['version'] = split_line[1]
        app_list.append(app)

    # For every app, get the remote URL's and the branches
    for app in app_list:
        app_path = full_bench_path + "/apps/" + app['name']
        # Get the remote URL
        out = check_output(["git", "remote", "-v"], cwd=app_path)
        list = out.decode("utf-8").splitlines()
        line = list[0].split()
        url = line[1]
        # Change SSH url's into HTTP url's
        url = url.replace("git@github.com:","https://github.com/")
        url = url.replace(".git","")
        app['repo-url'] = url

        # Get the main branch
        out = check_output(["git", "branch"], cwd=app_path)
        list = out.decode("utf-8").splitlines()

        main_branch = None
        for branch in list:
            asterisk = '*' in branch
            if asterisk:
                strings = branch.split()
                main_branch = strings[1]
                break
        app['branch'] = main_branch

    # For every app, grab latest version number from Github
    for app in app_list:
        # Build URL to get to __init__.py file, where version is defined
        url = app['repo-url'].replace("https://github.com/","https://raw.githubusercontent.com/")
        url += "/" + app['branch']
        url += "/" + app['name']
        url += "/__init__.py"
        app['attempted-init-url'] = url

        # Open url, and parse to find version
        latest_version = None
        try:
            data = urllib.request.urlopen(url) # it's a file like object and works just like a file
            for line in data: # files are iterable
                line_str = line.decode("utf-8")
                if "__version__" in line_str:
                    latest_version = line_str.split()[2]
                    latest_version = re.sub("'","",latest_version)
                    break
            app['latest-available-version-retrieval-success'] = 'Latest version retrieved'
        except urllib.error.HTTPError as err:
            if err.code == 404:
                app['latest-available-version-retrieval-success'] = 'Latest-version file not accessible'
                latest_version = 'latest-version-file-not-accessible'
            else:
                app['latest-available-version-retrieval-success'] = False
        except:
            print("other error in frappe_version_reporter.api.get_frappe_app_versions")
            app['latest-available-version-retrieval-success'] = False
        app['latest-available-version'] = latest_version

        # Compare the current and latest versions, to check if app is up to date
        if latest_version:
            if app['latest-available-version-retrieval-success'] == 'Latest version retrieved':
                if StrictVersion(app['version']) < StrictVersion(latest_version):
                    app['status'] = 'out-of-date'
                else:
                    app['status'] = 'up-to-date'
            else:
                app['status'] = 'latest-version-file-not-accessible'
        else:
            app['status'] = None

    if format == 'prtg':
        # Reformat list to acceptable PRTG JSON output
        prtg_obj = {}
        prtg_obj['prtg'] = {}
        prtg_obj['prtg']['result'] = {}
        for app in app_list:
            channel = {}
            channel['channel'] = app['name']
            if app['status']:
                if app['status'] == 'up-to-date':
                    channel['value'] = 1
                elif app['status'] == 'latest-version-file-not-accessible':
                    channel['value'] = 2
                elif app['status'] == 'out-of-date':
                    channel['value'] = 3
                else:
                    channel['value'] = 4
            else:
                channel['value'] = 4
            channel['valuelookup'] = 'vdl.frappeversioncheck'
            prtg_obj['prtg']['result'][app['name']] = channel
        return(prtg_obj)
    else:
        return(app_list)
