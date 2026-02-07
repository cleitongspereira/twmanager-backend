from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.router import api_router
from app.core.database import Base, engine


def create_app() -> FastAPI:
    app = FastAPI(title="FastAPI Auth Service")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "http://localhost:3000",
            "https://twmanager-frontend-producao.up.railway.app",
            "https://twmanager-frontend-desenvolvimento.up.railway.app",
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(api_router)
    return app


Base.metadata.create_all(bind=engine)

app = create_app()
