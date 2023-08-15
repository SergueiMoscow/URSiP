import sys

from services import read_from_xls, append_metrics, get_statistic
import logging
FILENAME = '/Users/sergey/sss23/work/URSIP/Приложение_к_заданию_бек_разработчика.xlsx'
year = 2023
month = 7

if __name__ == '__main__':
    data = read_from_xls(FILENAME, year, month)
    append_metrics(data, FILENAME)
    rows = get_statistic(2023, 7)
    print('Date       | Type | Forecast | Fact')
    for row in rows:
        print(
            f"{row.date} | {row.type.value}  |{row.forecast_q:9d} | {row.fact_q:9d}")
    logger = logging.getLogger()
    print(logger.getEffectiveLevel())
