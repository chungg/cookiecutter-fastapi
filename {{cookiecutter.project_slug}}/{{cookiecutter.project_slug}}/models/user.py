from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from {{cookiecutter.project_slug}}.db.base import Base


class User(Base):
    __tablename__ = 'auth_user'

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
