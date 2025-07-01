# 📎 Frappe WhatsApp PDF Plugin

This Frappe plugin app extends the [frappe_whatsapp](https://github.com/shridarpatil/frappe_whatsapp) integration to automatically generate and attach public PDF documents (like Sales Orders) to WhatsApp messages using Meta's document header templates.

---

## 📦 Features

- Automatically generates and attaches a **public PDF** (e.g., Sales Order) in WhatsApp messages.
- Designed for use with **Meta-approved message templates** that include a **document header**.
- Can be used with any DocType (Sales Order, Quotation, etc.) that has a print format.

---

## 🚀 Installation

From inside your Frappe bench:

```bash
cd ~/frappe-bench/apps
git clone https://github.com/miteshnandu/frappe_whatsapp_pdf.git
cd ~/frappe-bench
bench --site your-site-name install-app frappe_whatsapp_pdf
bench --site your-site-name migrate
bench restart
