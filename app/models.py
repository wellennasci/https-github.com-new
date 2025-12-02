from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from .database import Base

class WeatherReading(Base):
    __tablename__ = "weather_readings"

    id = Column(Integer, primary_key=True, index=True)
    city = Column(String(100), index=True)
    country = Column(String(10))
    temp = Column(Float)
    feels_like = Column(Float)
    humidity = Column(Integer)
    weather_main = Column(String(50))
    weather_description = Column(String(200))
    timestamp_utc = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)
