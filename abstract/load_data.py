from abc import ABC, abstractmethod
from datetime import date
from typing import NamedTuple

from typing_extensions import TypedDict

from db.model import Categories, Types, DataSources


class MetricsTuple(NamedTuple):
    date: date
    company: str
    category: Categories
    type: Types
    data: DataSources
    quantity: int


class LoadData(ABC):

    @abstractmethod
    def get_data(self) -> list[MetricsTuple]:
        pass
