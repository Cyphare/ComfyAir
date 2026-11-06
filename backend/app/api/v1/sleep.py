from fastapi import APIRouter
from app.schemas.sleep import SleepProfileRequest, SleepCurveResponse
from app.services.sleep_service import sleep_service

router = APIRouter(tags=["Sleep Mode"])


@router.post("/sleep-curve", response_model=SleepCurveResponse)
def get_sleep_temperature_curve(req: SleepProfileRequest):
    """
    Menghitung rekomendasi kurva temperatur tidur biologis dinamis sepanjang malam.
    """
    return sleep_service.calculate_sleep_curve(req)
