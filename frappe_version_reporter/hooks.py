# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "frappe_version_reporter"
app_title = "Frappe Version Reporter"
app_publisher = "Dirk van der Laarse"
app_description = "Enables method callable by API that reports app versions"
app_icon = "octicon octicon-versions"
app_color = "grey"
app_email = "dirk@laarse.co.za"
app_license = "GPL v3"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/frappe_version_reporter/css/frappe_version_reporter.css"
# app_include_js = "/assets/frappe_version_reporter/js/frappe_version_reporter.js"

# include js, css files in header of web template
# web_include_css = "/assets/frappe_version_reporter/css/frappe_version_reporter.css"
# web_include_js = "/assets/frappe_version_reporter/js/frappe_version_reporter.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "frappe_version_reporter.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "frappe_version_reporter.install.before_install"
# after_install = "frappe_version_reporter.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "frappe_version_reporter.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"frappe_version_reporter.tasks.all"
# 	],
# 	"daily": [
# 		"frappe_version_reporter.tasks.daily"
# 	],
# 	"hourly": [
# 		"frappe_version_reporter.tasks.hourly"
# 	],
# 	"weekly": [
# 		"frappe_version_reporter.tasks.weekly"
# 	]
# 	"monthly": [
# 		"frappe_version_reporter.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "frappe_version_reporter.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "frappe_version_reporter.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "frappe_version_reporter.task.get_dashboard_data"
# }

