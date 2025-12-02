from datetime import datetime
import requests
from .config import settings
from .schemas import WeatherReadingCreate

class WeatherAPIError(Exception):
    pass

def fetch_weather_by_city(city: str) -> WeatherReadingCreate:
    if not settings.openweather_api_key:
        raise WeatherAPIError("OPENWEATHER_API_KEY não configurada.")

    params = {
        "q": city,
        "appid": settings.openweather_api_key,
        "units": "metric",
        "lang": "pt_br",
    }

    resp = requests.get(settings.openweather_base_url, params=params, timeout=10)

    if resp.status_code != 200:
        raise WeatherAPIError(f"Erro ao chamar OpenWeather: {resp.status_code} - {resp.text}")

    data = resp.json()
    ts = datetime.utcfromtimestamp(data["dt"])

    return WeatherReadingCreate(
        city=data["name"],
        country=data["sys"]["country"],
        temp=data["main"]["temp"],
        feels_like=data["main"]["feels_like"],
        humidity=data["main"]["humidity"],
        weather_main=data["weather"][0]["main"],
        weather_description=data["weather"][0]["description"],
        timestamp_utc=ts,
    )
