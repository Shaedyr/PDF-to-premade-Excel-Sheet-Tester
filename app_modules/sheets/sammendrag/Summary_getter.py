def generate_company_summary(data: dict) -> str:
    name = data.get("name", "")
    orgnr = data.get("orgnr", "")
    return f"{name} (Org.nr {orgnr})"

def place_summary(ws, summary_text: str, cell: str):
    ws[cell] = summary_text