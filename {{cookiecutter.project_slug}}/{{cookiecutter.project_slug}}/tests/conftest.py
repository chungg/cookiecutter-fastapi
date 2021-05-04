from typing import Dict, Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from {{cookiecutter.project_slug}}.api import deps
from {{cookiecutter.project_slug}}.db import Base
from {{cookiecutter.project_slug}}.main import app
from {{cookiecutter.project_slug}}.tests.utils import user as user_utils

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)


@pytest.fixture(scope="session")
def db() -> Generator:
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


@pytest.fixture(scope="module")
def client() -> Generator:

    def _get_db_override():
        try:
            db = TestingSessionLocal()
            yield db
        finally:
            db.close()

    app.dependency_overrides[deps.get_db] = _get_db_override
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="module")
def superuser_token_headers(client: TestClient, db: Session) -> Dict[str, str]:
    return user_utils.authentication_token_from_email(
        client=client, email=user_utils.TEST_SUPERUSER, db=db, is_superuser=True
    )


@pytest.fixture(scope="module")
def normal_user_token_headers(client: TestClient, db: Session) -> Dict[str, str]:
    return user_utils.authentication_token_from_email(
        client=client, email=user_utils.TEST_USER, db=db
    )
