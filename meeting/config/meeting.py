from __future__ import unicode_literals
from frappe import _
from frappe.desk.moduleview import add_setup_section


def get_data():
	data = [
		{
			"label": _("Meeting"),
			"icon": "fa fa-star",
			"items": [
				{
					"type": "doctype",
					"name": "Meeting",	
					"description": _("Content web page."),
					"onboard": 1,
				}
			]
		}
	]
	add_setup_section(data, "meeting", "Meeting", _("Meeting"), "fa fa-globe")
	return data
