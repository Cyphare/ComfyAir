from typing import List
from app.schemas.sleep import (
    SleepProfileRequest,
    SleepHourlyPoint,
    SleepCurveResponse,
)


class SleepService:
    def calculate_sleep_curve(self, req: SleepProfileRequest) -> SleepCurveResponse:
        """
        Menghitung kurva temperatur tidur biologis sepanjang malam:
        1. Fase Awal (Sleep Onset): Suhu sejuk (start_temp) memicu pelepasan melatonin & kantuk.
        2. Fase Deep Sleep (NREM): Suhu dinaikkan (deep_sleep_temp) mengikuti penurunan metabolisme tubuh,
           sekaligus menghemat energi kompresor AC hingga 15-20%.
        3. Fase Menjelang Bangun: Disesuaikan ke wake_temp untuk kesegaran bangun tidur.
        """
        bed_hour = int(req.bedtime.split(":")[0])
        wake_hour = int(req.wake_time.split(":")[0])

        hours_sequence: List[int] = []
        current = bed_hour
        while True:
            hours_sequence.append(current)
            if current == wake_hour:
                break
            current = (current + 1) % 24

        total_hours = len(hours_sequence) - 1
        if total_hours <= 0:
            total_hours = 8

        curve: List[SleepHourlyPoint] = []
        for i, hour in enumerate(hours_sequence):
            ratio = i / (len(hours_sequence) - 1) if len(hours_sequence) > 1 else 0

            if ratio < 0.25:
                # 25% awal tidur
                temp = req.start_temp
                phase = "Fase Awal Tidur (Sleep Onset)"
            elif ratio < 0.75:
                # 50% tengah malam (Deep sleep)
                temp = req.deep_sleep_temp
                phase = "Fase Deep Sleep (NREM)"
            else:
                # 25% akhir menjelang bangun
                temp = req.wake_temp
                phase = "Fase Menjelang Bangun (REM)"

            curve.append(
                SleepHourlyPoint(
                    time=f"{hour:02d}:00",
                    recommended_temp=temp,
                    phase=phase,
                )
            )

        return SleepCurveResponse(
            summary=(
                f"Kurva tidur dioptimalkan dari {req.bedtime} sampai {req.wake_time} "
                f"dengan variasi suhu {req.start_temp}°C -> {req.deep_sleep_temp}°C -> {req.wake_temp}°C"
            ),
            total_sleep_hours=total_hours,
            curve=curve,
            estimated_energy_saving="Estimasi penghematan energi ~15-20% dibanding suhu konstan",
        )


sleep_service = SleepService()
