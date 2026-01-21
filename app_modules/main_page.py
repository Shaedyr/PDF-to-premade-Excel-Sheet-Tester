import streamlit as st
from openpyxl import load_workbook

from app_modules.template_loader import load_template
from app_modules.sheets.sammendrag.BRREG_info_getter import fetch_company_by_org
from app_modules.sheets.sammendrag.BRREG_Proff_info_getter_merger import merge_company_data
from app_modules.sheets.sammendrag.Summary_info_getter import generate_company_summary, place_summary
from app_modules.pdf_parser import extract_fields_from_pdf
from app_modules.excel_filler import fill_excel
from app_modules.input import get_user_inputs

def run():
    st.title("PDF → Excel")
    pdf_bytes, selected_company = get_user_inputs()