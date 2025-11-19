import frappe

def check_app_permission():
    return False

def get_role_permission(user):
    return "(`tabRole`.name not in ('Academics User','Studio User','Interviewer','Analytics','Support Team','Fulfillment User','Quality Manager','Delivery User','Fleet Manager','Delivery Manager','Manufacturing User','Projects User','Projects Manager','Manufacturing Manager','Translator','Maintenance User','Maintenance Manager','Knowledge Base Editor','Knowledge Base Contributor','Newsletter Manager','Marketing Manager','Blogger','Inbox User','Dashboard Manager','Website Manager') )"

def get_module_def_permission(user):
    return "(`tabModule Def`.name not in ('CRM','EDI','Projects','Website','Regional','Communication','ERPNext Integrations') )"

def get_language_permission(user):
    return "(`tabLanguage`.name  in ('en','km') )"
