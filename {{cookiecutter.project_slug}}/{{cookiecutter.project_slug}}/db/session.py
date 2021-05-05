from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from {{cookiecutter.project_slug}}.core.config import settings

engine = create_engine(settings.DATABASE_URI, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
