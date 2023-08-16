import datetime
import logging
from datetime import date
from typing import List, NamedTuple

from sqlalchemy import func
from sqlalchemy.orm import aliased

from abstract.load_data import MetricsTuple
from db.enums import Categories, Types
from db.model import Log, Metrics, session
from import_data.from_xls import LoadFromXLSX


class StatisticItem(NamedTuple):
    date: date
    category: Categories
    type: Types
    fact_q: int
    forecast_q: int


def read_from_xls(filename, year: int, month: int) -> list[MetricsTuple]:
    """Loads data from source, appending test dates"""
    return LoadFromXLSX(
        source_file_name=filename,
        year=year,
        month=month
    ).get_data()


def append_metrics(rows: list[MetricsTuple], source: str) -> None:
    """Appends records to forecast table from list of MetricsTuple
    source is received for check if  data from original file already was loades into table
    """
    if not is_loaded_metrics(source):
        for row in rows:
            metric_dict = dict(row._asdict())
            new_metric = Metrics(**metric_dict)
            session.add(new_metric)
        session.add(Log(date=datetime.datetime.today(), source=source))
        session.commit()
        logging.info(f'Source {source} loaded successfully')
    else:
        logging.warning(f'Source {source} already loaded')


def is_loaded_metrics(source: str):
    """Check if data from source is already loaded"""
    row = session.query(Log).filter(Log.source == source).all()
    return len(row) > 0


def get_statistic(year: int, month: int) -> List[StatisticItem]:
    """Selects data from forecast table for statistics grouping by date and type (liq, oil)"""
    fact = aliased(Metrics)
    forecast = aliased(Metrics)

    result = session.query(
        fact.date,
        fact.category,
        fact.type,
        func.sum(fact.quantity).label('fact_q'),
        func.sum(forecast.quantity).label('forecast_q'),
    ).join(
        forecast,
        (fact.date == forecast.date) &
        (fact.type == forecast.type)
    ).filter(
        fact.category == Categories.fact,
        forecast.category == Categories.forecast,
        func.strftime('%Y', fact.date) == str(year),
        func.strftime('%m', fact.date) == f'{month:02d}'
    ).group_by(
        fact.date,
        fact.category,
        fact.type,
    ).all()

    return result
