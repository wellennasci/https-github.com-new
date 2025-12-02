

from sqlalchemy import create_engine

url = "postgresql+psycopg2://postgres:tomate@localhost:5432/weather_db"

engine = create_engine(url)

try:
    conn = engine.connect()
    print("Conexão OK!")
    conn.close()
except Exception as e:
    print("Erro ao conectar:")
    print(e)
