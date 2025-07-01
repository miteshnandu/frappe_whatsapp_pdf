import frappe
from frappe.utils.pdf import get_pdf
from frappe.utils.file_manager import save_file
from frappe.utils import get_url

@frappe.whitelist()
def generate_whatsapp_pdf(docname, doctype):
    doc = frappe.get_doc(doctype, docname)
    pdf_data = get_pdf(doc.get_html())
    filename = f"{docname}.pdf"
    file = save_file(filename, pdf_data, doctype, docname, is_private=0)

    return {
        "link": get_url(file.file_url),
        "filename": filename
    }
