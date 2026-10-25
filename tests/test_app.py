from app import validate_invoice

def test_missing_vendor_flagged(): assert any('vendor' in x for x in validate_invoice({'invoice_number':'1','amount':10}))
def test_negative_amount_flagged(): assert any('negative' in x for x in validate_invoice({'invoice_number':'1','vendor':'A','amount':-1}))
