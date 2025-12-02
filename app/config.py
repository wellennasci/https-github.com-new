import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    def __init__(self):
        self.openweather_api_key = os.getenv("OPENWEATHER_API_KEY")
        self.openweather_base_url = "https://api.openweathermap.org/data/2.5/weather"
        self.db_url = os.getenv(
            "DATABASE_URL",
            "postgresql+psycopg2://postgres:postgres@localhost:5432/weather_db"
        )

settings = Settings()
