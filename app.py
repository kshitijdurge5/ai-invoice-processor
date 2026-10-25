import streamlit as st
from portfolio_visuals import render_visuals
def validate_invoice(invoice: dict) -> list[str]:
    issues = []
    for key in ("invoice_number", "vendor", "amount"):
        if key not in invoice or invoice[key] in ("", None):
            issues.append(f"Missing required field: {key}")
    try:
        if float(invoice.get("amount", 0)) < 0: issues.append("Amount cannot be negative.")
    except (TypeError, ValueError):
        issues.append("Amount must be numeric.")
    return issues

st.set_page_config(page_title="Invoice Validator", page_icon="ðŸ§¾")
render_visuals('09_invoice_processor')
st.title("Invoice Data Validator")
st.caption("Enter extracted fields manually; OCR and file extraction are future extensions.")
number = st.text_input("Invoice number")
vendor = st.text_input("Vendor")
amount = st.text_input("Amount")
if st.button("Validate"):
    issues = validate_invoice({"invoice_number": number, "vendor": vendor, "amount": amount})
    if issues: st.error("\n".join(issues))
    else: st.success("Basic validation passed. A human must still verify the invoice.")

