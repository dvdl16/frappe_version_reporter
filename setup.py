# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in frappe_version_reporter/__init__.py
from frappe_version_reporter import __version__ as version

setup(
	name='frappe_version_reporter',
	version=version,
	description='Enables method callable by API that reports app versions',
	author='Dirk van der Laarse',
	author_email='dirk@laarse.co.za',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
