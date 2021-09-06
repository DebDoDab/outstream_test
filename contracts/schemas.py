from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, Field, validator


class ContractReplacementsFields:
    """Class for replacing text in contract template"""

    FULL_NAME = "{fullName}"
    COMPANY_TITLE = "{companyTitle}"
    ADDRESS = "{address}"
    CONTRACT_DATE = "{contractDate}"

    FIELDS = [
        FULL_NAME,
        COMPANY_TITLE,
        ADDRESS,
        CONTRACT_DATE,
    ]


class GoogleDoc(BaseModel):
    """Google document class for using google docs API"""

    document_id: str


class GoogleDocReplacement(BaseModel):
    """Replace class for google docs API"""

    search: str
    replace: str


class ContractReplacements(BaseModel):
    """Custom replacements in template google document"""

    full_name: str
    company_title: str
    address: str
    contract_date: Optional[date] = None

    @validator("date", pre=True)
    def parse_date(cls, v):
        if isinstance(v, str):
            return date.fromtimestamp(datetime.strptime(v, "%Y-%m-%d").timestamp())
        elif v is None:
            return datetime.now().date()

        raise ValueError(f"Has to be string in format YYYY-MM-DD, got {v} instead")
