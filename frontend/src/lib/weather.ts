import { fetchJson } from "./http";

// Current conditions for Yogyakarta. Open-Meteo answers in local Jakarta time
// (e.g. "2026-10-03T20:15") and refreshes the current block every 15 minutes.
export const OPEN_METEO_URL =
  "https://api.open-meteo.com/v1/forecast?latitude=-7.7956&longitude=110.3695" +
  "&current=temperature_2m,relative_humidity_2m&timezone=Asia%2FJakarta";

export type CurrentWeather = {
  temp: number;
  humidity: number;
  /** Observation time as printed on the page, "20.15". */
  observedAt: string;
};

export async function fetchCurrentWeather(signal: AbortSignal): Promise<CurrentWeather> {
  const data = await fetchJson(OPEN_METEO_URL, { timeoutMs: 3000, signal });

  const current =
    typeof data === "object" && data !== null ? (data as Record<string, unknown>).current : null;
  if (typeof current !== "object" || current === null) throw new Error("Missing current block");

  const {
    temperature_2m: temp,
    relative_humidity_2m: humidity,
    time,
  } = current as Record<string, unknown>;

  if (typeof temp !== "number" || !Number.isFinite(temp) || temp < -10 || temp > 50) {
    throw new Error("Unexpected temperature_2m");
  }
  if (typeof humidity !== "number" || !Number.isFinite(humidity) || humidity < 0 || humidity > 100) {
    throw new Error("Unexpected relative_humidity_2m");
  }
  if (typeof time !== "string" || time.length < 16) throw new Error("Unexpected time");

  return { temp, humidity, observedAt: time.slice(11, 16).replace(":", ".") };
}
