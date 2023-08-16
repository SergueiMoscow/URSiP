from sqlalchemy import (Column, Date, Enum, Index, Integer, String,
                        create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from db.enums import Categories, DataSources, Types
from settings import DATABASE

engine = create_engine(DATABASE, echo=False)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Metrics(Base):
    """
    Фактические и прогнозные данные Qlic, Qoil
    """
    __tablename__ = 'forecast'

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    company = Column(String(255))
    category = Column(Enum(Categories))
    type = Column(Enum(Types))
    data = Column(Enum(DataSources))
    quantity = Column(Integer)


class Log(Base):
    """
    Лог импортированных данных в Metrics
    """

    __tablename__ = 'log'

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    source = Column(String)


date_index = Index('idx_date', Metrics.date)
source_index = Index('log_source', Log.source)
