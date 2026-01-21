from app_modules.sheets.sammendrag.BRREG_info_getter import format_company_data
from app_modules.sheets.sammendrag.Proff_info_getter import get_Proff_data

def merge_company_data(orgnr: str) -> dict:
    brreg = format_company_data(fetch_company_by_org(orgnr))
    proff = get_Proff_data(orgnr)

    return {
        **brreg,
        **proff
    }