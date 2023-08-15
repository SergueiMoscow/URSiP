from enum import Enum


class Categories(Enum):
    fact = 'fact'
    forecast = 'forecast'


class Types(Enum):
    liq = 'liq'
    oil = 'oil'


class DataSources(Enum):
    data1 = 'data1'
    data2 = 'data2'
