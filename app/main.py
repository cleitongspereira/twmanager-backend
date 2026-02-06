from fastapi import FastAPI
from app.api.v1.router import api_router
from app.core.database import Base, engine

def create_app() -> FastAPI:
    app = FastAPI(title="FastAPI Auth Service")
    app.include_router(api_router)
    return app

Base.metadata.create_all(bind=engine)

app = create_app()
