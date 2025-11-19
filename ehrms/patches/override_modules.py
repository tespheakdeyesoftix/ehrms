# my_app/patches/override_modules.py
import frappe
from frappe.utils import modules as modules_module

def get_modules_from_app(app):
	exclude_modules = ["CRM","EDI","Projects","Website","Regional","Communication","ERPNext Integrations","HR"]
	
	return frappe.get_all("Module Def", filters={"app_name": app,"name":["not in",exclude_modules]}, fields=["module_name", "app_name as app"])

# Override the original function
modules_module.get_modules_from_app = get_modules_from_app
