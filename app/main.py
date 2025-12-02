from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from .database import Base, engine, get_db
from .models import WeatherReading
from .schemas import WeatherReadingOut
from .weather_service import fetch_weather_by_city, WeatherAPIError

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Weather API - Avaliação Técnica",
    version="1.0.0",
)

@app.post("/weather/refresh", response_model=WeatherReadingOut)
def refresh_weather(
    city: str = Query(...),
    db: Session = Depends(get_db),
):
    try:
        weather_data = fetch_weather_by_city(city)
    except WeatherAPIError as e:
        raise HTTPException(status_code=400, detail=str(e))

    record = WeatherReading(**weather_data.dict())
    db.add(record)
    db.commit()
    db.refresh(record)
    return record

@app.get("/weather", response_model=List[WeatherReadingOut])
def list_weather(
    city: Optional[str] = Query(None),
    db: Session = Depends(get_db),
):
    query = db.query(WeatherReading)
    if city:
        query = query.filter(WeatherReading.city.ilike(f"%{city}%"))
    return query.order_by(WeatherReading.created_at.desc()).all()
