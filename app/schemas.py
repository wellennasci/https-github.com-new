from datetime import datetime
from pydantic import BaseModel

class WeatherReadingBase(BaseModel):
    city: str
    country: str
    temp: float
    feels_like: float
    humidity: int
    weather_main: str
    weather_description: str
    timestamp_utc: datetime

class WeatherReadingCreate(WeatherReadingBase):
    pass

class WeatherReadingOut(WeatherReadingBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
