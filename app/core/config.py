import os

class Settings:
    POSTGRES_HOST = os.getenv("PGHOST")
    POSTGRES_PORT = os.getenv("PGPORT")
    POSTGRES_USER = os.getenv("PGUSER")
    POSTGRES_PASSWORD = os.getenv("PGPASSWORD")
    POSTGRES_DB = os.getenv("PGDATABASE")

settings = Settings()