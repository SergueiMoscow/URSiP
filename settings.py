import logging
import os

BASE_DIR = os.path.join(os.path.dirname(__file__))
LOG_FILE = os.path.join(BASE_DIR, 'logs', 'import.log')
LOG_LEVEL = logging.WARNING

DATABASE = 'sqlite:///' + os.path.join(BASE_DIR, 'forecast.db')
logging.basicConfig(filename=LOG_FILE,
                    format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=LOG_LEVEL)
