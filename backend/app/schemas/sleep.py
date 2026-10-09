from typing import List, Optional
from pydantic import BaseModel, Field


class SleepProfileRequest(BaseModel):
    bedtime: str = Field(
        default="22:00",
        example="22:00",
        description="Jam tidur (format HH:MM)",
    )
    wake_time: str = Field(
        default="06:00",
        example="06:00",
        description="Jam bangun (format HH:MM)",
    )
    start_temp: int = Field(
        default=24,
        ge=18,
        le=30,
        example=24,
        description="Suhu awal menjelang tidur (°C)",
    )
    deep_sleep_temp: int = Field(
        default=26,
        ge=18,
        le=30,
        example=26,
        description="Suhu saat fase deep sleep (°C)",
    )
    wake_temp: int = Field(
        default=25,
        ge=18,
        le=30,
        example=25,
        description="Suhu saat bangun tidur (°C)",
    )
    user_id: Optional[str] = Field(
        default=None,
        description="UUID pengguna dari Supabase jika terdaftar",
    )


class SleepHourlyPoint(BaseModel):
    time: str = Field(..., example="23:00", description="Jam tertentu")
    recommended_temp: int = Field(
        ..., example=25, description="Rekomendasi setpoint suhu AC (°C)"
    )
    phase: str = Field(
        ...,
        example="Fase Awal Tidur (Sleep Onset)",
        description="Fase biologis tidur",
    )


class SleepCurveResponse(BaseModel):
    summary: str = Field(
        ..., example="Kurva temperatur tidur biologis berhasil dihitung"
    )
    total_sleep_hours: int = Field(
        ..., example=8, description="Durasi tidur dalam jam"
    )
    curve: List[SleepHourlyPoint] = Field(
        ..., description="Daftar titik rekomendasi suhu per jam"
    )
    estimated_energy_saving: str = Field(
        ..., example="Estimasi penghematan energi ~15-20% dibanding suhu flat"
    )
