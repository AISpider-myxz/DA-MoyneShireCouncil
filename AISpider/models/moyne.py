from sqlalchemy import Column, String, Text, Integer, DateTime, func
from .metadata_base import Base


class Moyne(Base):
    __tablename__ = 'moyne'

    id = Column(Integer, primary_key=True, autoincrement=True)

    app_number = Column(String(256), nullable=False, unique=True)
    description = Column(Text, nullable=True, server_default=None)
    address = Column(Text, nullable=True, server_default=None)
    documents = Column(Text, nullable=True, server_default=None)
    _tid = Column(String(255), nullable=False,server_default=None )
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())