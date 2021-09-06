from fastapi import APIRouter

from api.contract_views import contract_router

api_router = APIRouter()

api_router.include_router(contract_router, prefix="/contract", tags=["contract"])
