from frappe_whatsapp.api.whatsapp import send_whatsapp as base_send_whatsapp
import frappe

def send_whatsapp(*args, **kwargs):
    res = base_send_whatsapp(*args, **kwargs)

    docname = kwargs.get("name")
    doctype = kwargs.get("doctype")

    if not docname or not doctype:
        return res

    pdf_info = frappe.call("frappe_whatsapp_pdf.api.pdf.generate_whatsapp_pdf", docname=docname, doctype=doctype)

    for msg in res.get("messages", []):
        if msg["type"] == "template":
            msg["template"].setdefault("components", [])
            msg["template"]["components"].insert(0, {
                "type": "header",
                "parameters": [{
                    "type": "document",
                    "document": {
                        "link": pdf_info["link"],
                        "filename": pdf_info["filename"]
                    }
                }]
            })

    return res
