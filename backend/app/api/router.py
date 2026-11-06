from fastapi import APIRouter
from app.api.v1 import predict, sleep

api_router = APIRouter()
api_router.include_router(predict.router)
api_router.include_router(sleep.router)
