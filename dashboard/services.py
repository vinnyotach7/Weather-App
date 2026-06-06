import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.weather-ai.co/v1/weather"
API_KEY = os.getenv("WEATHER_AI_API_KEY")


def get_weather(lat, lon, days=7, ai=True, units="metric", lang="en"):
    if not API_KEY:
        return {
            "error": "Missing API key",
            "details": "WEATHER_AI_API_KEY not set"
        }

    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }

    params = {
        "lat": lat,
        "lon": lon,
        "days": days,
        "ai": str(ai).lower(),
        "units": units,
        "lang": lang
    }

    try:
        response = requests.get(BASE_URL, params=params, headers=headers, timeout=10)
    except requests.exceptions.RequestException as e:
        return {
            "error": "Request failed",
            "details": str(e)
        }

    if response.status_code != 200:
        return {
            "error": "Weather API failed",
            "status_code": response.status_code,
            "details": response.text
        }

    raw = response.json()

    # -------------------------
    # SAFE NORMALIZATION
    # -------------------------
    current = (
        raw.get("current")
        or raw.get("data", {}).get("current")
        or raw
    )

    temperature = current.get("temperature") or current.get("temp")

    humidity = current.get("humidity")
    if humidity is None:
        humidity = 65  # fallback default

    wind_speed = current.get("wind_speed") or current.get("wind") or 0

    condition = (
        current.get("condition", {}).get("text")
        if isinstance(current.get("condition"), dict)
        else current.get("condition")
    )

    if not condition:
        condition = current.get("weather", {}).get("description")

    if not condition:
        condition = "Unknown"

    # OPTIONAL: forecast safe extraction
    forecast = raw.get("forecast", [])

    return {
        "temperature": temperature,
        "humidity": humidity,
        "wind_speed": wind_speed,
        "condition": condition,
        "forecast": forecast
    }