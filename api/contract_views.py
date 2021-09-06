from fastapi import APIRouter, Query
from fastapi.encoders import jsonable_encoder
from pydantic import ValidationError
from starlette import status
from io import BytesIO
from starlette.responses import JSONResponse, StreamingResponse

from contracts.schemas import ContractReplacements
from contracts.services import get_pdf_contract

contract_router = APIRouter()


@contract_router.get("/", response_model=StreamingResponse)
async def make_contract(replacements: ContractReplacements):
    """Returns custom contract made from template google document"""
    pdf_contract_raw = get_pdf_contract(replacements)

    return StreamingResponse(BytesIO(pdf_contract_raw), media_type="application/pdf")
