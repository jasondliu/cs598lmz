import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import os
import sys
import datetime
import logging
import time
import json
import traceback
import re

import requests
from bs4 import BeautifulSoup

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import *


SCRIPT_ROOT = os.path.abspath(os.path.dirname(__file__))

logging.basicConfig(
    filename=os.path.join(SCRIPT_ROOT, 'logs/{}.log'.format(datetime.date.today())),
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

ENGINE = create_engine(
    "mysql+pymysql://root:root@localhost:3306/douban?charset=utf8mb4",
    echo=False,
    max_overflow=5
)

