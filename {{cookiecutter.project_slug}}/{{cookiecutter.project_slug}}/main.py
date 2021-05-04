from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from {{cookiecutter.project_slug}}.api.v1.api import api_router
from {{cookiecutter.project_slug}}.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    docs_url='/docs',
    redoc_url='/redoc',
)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=settings.API_V1_STR)
