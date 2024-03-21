"""This module contains the SQLAlchemy model for the Todo item."""
from datetime import datetime

from settings import Base
from sqlalchemy import Column, DateTime, Integer, String


class TodoModel(Base):
    """Represents a Todo item in the application.
    """

    __tablename__ = 'todo'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
