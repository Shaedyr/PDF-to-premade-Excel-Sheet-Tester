from app_modules.Sheets.Sammendrag.BRREG_info_getter import fetch_company_by_org, format_company_data
from app_modules.Sheets.Sammendrag.Proff_info_getter import get_Proff_data
import streamlit as st


def merge_company_data(org_number: str) -> dict:
    st.write("MERGER STARTED")

    BRREG_data = format_company_data(fetch_company_by_org(org_number)) or {}
    Proff_data = get_Proff_data(org_number) or {}

    st.write("PROFF DATA RECEIVED:", Proff_data)

    merged = BRREG_data.copy()

    # Override ALL financial fields from Proff
    financial_keys = [
        "revenue_2024",
        "driftsresultat_2024",
        "resultat_for_skatt_2024",
        "sum_eiendeler_2024",
        "egenkapital_2024",
    ]

    for key in financial_keys:
        if key in Proff_data:
            merged[key] = Proff_data[key]

    # Fill missing fields from Proff
    for key, value in Proff_data.items():
        if key not in merged or merged[key] in (None, "", 0):
            merged[key] = value

    st.write("MERGED KEYS:", list(merged.keys()))

    return merged
