import frappe


def check_hrms_app_permission():
	return True
	"""Check if user has permission to access the app (for showing the app on app screen)"""
	if frappe.session.user == "Administrator":
		return True


	return False

def check_erpnext_app_permission():
	return True
	"""Check if user has permission to access the app (for showing the app on app screen)"""
	if frappe.session.user == "Administrator":
		return True


	return False




def get_modules_from_all_apps():
	frappe.msgprint("hello")
	modules_list = []
	for app in frappe.get_installed_apps():
		modules_list += get_modules_from_app(app)
	return modules_list

def get_modules_from_app(app):
	exlude_modules = [
		"EDI","Portal","CRM"
	]
	return frappe.get_all("Module Def", filters={"app_name": app, "name": ["not in", exlude_modules]}, fields=["module_name", "app_name as app"])

