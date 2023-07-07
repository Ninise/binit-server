from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db.base_class import Base

if TYPE_CHECKING:
    from .feedback import Feedback


class Feedback(Base):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, index=True)
    message = Column(String, index=True)