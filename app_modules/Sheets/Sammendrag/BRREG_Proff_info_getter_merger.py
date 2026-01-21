from app_modules.Sheets.Sammendrag.BRREG_info_getter import fetch_company_by_org, format_company_data
from app_modules.Sheets.Sammendrag.Proff_info_getter import get_Proff_data
import streamlit as st


def merge_company_data(org_number: str) -> dict:
    st.write("MERGER STARTED")

    # --- Fetch data ---
    BRREG_data = format_company_data(fetch_company_by_org(org_number)) or {}
    Proff_data = get_Proff_data(org_number) or {}

    st.write("BRREG DATA:", BRREG_data)
    st.write("PROFF RAW DATA:", Proff_data)

    merged = BRREG_data.copy()

    # ---------------------------------------------------------
    # 1. BRREG revenue stays in B12 → key: revenue_2024
    # 2. Proff revenue goes to E11 → key: revenue_2024_proff
    # ---------------------------------------------------------
    if "revenue_2024" in Proff_data:
        merged["revenue_2024_proff"] = Proff_data["revenue_2024"]

    # ---------------------------------------------------------
    # 3. Merge all financial years (2024–2022)
    # ---------------------------------------------------------
    financial_keys = [
        "revenue_2024", "revenue_2023", "revenue_2022",
        "driftsresultat_2024", "driftsresultat_2023", "driftsresultat_2022",
        "resultat_for_skatt_2024", "resultat_for_skatt_2023", "resultat_for_skatt_2022",
        "sum_eiendeler_2024", "egenkapital_2024"
    ]

    for key in financial_keys:
        if key in Proff_data:
            merged[key] = Proff_data[key]

    # ---------------------------------------------------------
    # 4. Fill missing fields from Proff (homepage, etc.)
    # ---------------------------------------------------------
    for key, value in Proff_data.items():
        if key not in merged or merged[key] in (None, "", 0):
            merged[key] = value

    st.write("MERGED KEYS:", list(merged.keys()))
    st.write("FINAL MERGED DATA:", merged)

    return merged
