# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "Frappe Version Reporter",
			"color": "grey",
			"icon": "octicon octicon-versions",
			"type": "module",
			"label": _("Frappe Version Reporter")
		}
	]
