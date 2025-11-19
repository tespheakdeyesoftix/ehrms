import frappe
def after_install():
    disable_role()
    setup_language()

def disable_role():
    roles =["Studio User","Interviewer","Analytics","Support Team","Fulfillment User","Quality Manager","Delivery User","Fleet Manager","Delivery Manager","Academics User","Manufacturing User","Projects User","Projects Manager","Manufacturing Manager","Translator","Maintenance User","Maintenance Manager","Knowledge Base Editor","Knowledge Base Contributor","Newsletter Manager"]
    frappe.db.sql("update `tabRole` set disabled = 1 where name in %(roles)s",{"roles": roles})
    frappe.db.commit()

def setup_language():
    frappe.db.sql("update `tabLanguage` set enabled = 1 where name in ('en','km')")
    frappe.db.commit()
    