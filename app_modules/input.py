import streamlit as st
from app_modules.sheets.sammendrag.BRREG_info_getter import search_BRREG_live

def get_user_inputs():
    st.header("1️⃣ Last opp PDF og velg selskap")

    col1, col2 = st.columns(2)

    with col1:
        pdf_file = st.file_uploader("PDF dokument", type="pdf")
        pdf_bytes = pdf_file.read() if pdf_file else None

    with col2:
        query = st.text_input("Selskapsnavn")
        selected_company = None

        if query and len(query) >= 2:
            results = search_BRREG_live(query)

            if results:
                labels = []
                mapping = {}

                for c in results:
                    name = c.get("navn", "")
                    org = c.get("organisasjonsnummer", "")
                    label = f"{name} ({org})"
                    labels.append(label)
                    mapping[label] = c

                choice = st.selectbox("Velg selskap", labels)
                selected_company = mapping.get(choice)

    return pdf_bytes, selected_company

def run():
    st.title("Input-modul")