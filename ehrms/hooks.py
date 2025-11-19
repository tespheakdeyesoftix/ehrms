app_name = "ehrms"
app_title = "ESTC Human Resource"
app_publisher = "Tes Pheakdey"
app_description = "ESTC Human Resource"
app_email = "pheakdey.micronet@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "ehrms",
# 		"logo": "/assets/ehrms/images/ehrms_logo.png",
# 		"title": "eHRMS",
# 		"route": "/app/ehrms",
# 		"has_permission": "ehrms.permission.check_app_permission"
# 	}
# ]


# update hook in hrms app 
from  erpnext import hooks as erpnext 
from hrms import hooks as hrms
import frappe

hrms.add_to_apps_screen = [
	{
		"name": "hrms",
		"logo": "/assets/ehrms/images/ehrms_logo.png",
		"title": "eHRMS",
		"route": "/app/staffing",
		"has_permission": "ehrms.overrides.utils.check_hrms_app_permission",
	}
]


# erpnext.add_to_apps_screen  = [
# 	{
# 		"name": "ePOS",
# 		"logo": "/assets/erpnext/images/erpnext-logo.svg",
# 		"title": "ePOS",
# 		"route": "/home",
# 		"has_permission": "ehrms.overrides.utils.check_erpnext_app_permission",
# 	}
# ]




 
# *******************Monkey Patch**********************
import ehrms.patches.override_modules


# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = "/assets/ehrms/css/ehrms.css"
# app_include_js = "/assets/ehrms/js/ehrms.js"

# include js, css files in header of web template
# web_include_css = "/assets/ehrms/css/ehrms.css"
# web_include_js = "/assets/ehrms/js/ehrms.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "ehrms/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "ehrms/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "ehrms.utils.jinja_methods",
# 	"filters": "ehrms.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "ehrms.install.before_install"
after_install = "ehrms.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "ehrms.uninstall.before_uninstall"
# after_uninstall = "ehrms.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "ehrms.utils.before_app_install"
# after_app_install = "ehrms.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "ehrms.utils.before_app_uninstall"
# after_app_uninstall = "ehrms.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "ehrms.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

permission_query_conditions = {
	"Role": "ehrms.permission.get_role_permission",
	"Module Def": "ehrms.permission.get_module_def_permission",
	"Language": "ehrms.permission.get_language_permission",
}

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
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"ehrms.tasks.all"
# 	],
# 	"daily": [
# 		"ehrms.tasks.daily"
# 	],
# 	"hourly": [
# 		"ehrms.tasks.hourly"
# 	],
# 	"weekly": [
# 		"ehrms.tasks.weekly"
# 	],
# 	"monthly": [
# 		"ehrms.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "ehrms.install.before_tests"

# Overriding Methods
# ------------------------------
#
override_whitelisted_methods = {
	"hrms.hr.utils.check_app_permission": "ehrms.overrides.utils.check_hrms_app_permission",
	"erpnext.check_app_permission": "ehrms.overrides.utils.check_erpnext_app_permission",
	"frappe.utils.modules.get_modules_from_all_apps": "ehrms.overrides.utils.get_modules_from_all_apps",
	"hrms.hr.dashboard_chart_source.hiring_vs_attrition_count.hiring_vs_attrition_count.get_data": "ehrms.overrides.dashboard_chart_source.hiring_vs_attrition_count.get_data"
}

#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "ehrms.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["ehrms.utils.before_request"]
# after_request = ["ehrms.utils.after_request"]

# Job Events
# ----------
# before_job = ["ehrms.utils.before_job"]
# after_job = ["ehrms.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"ehrms.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

