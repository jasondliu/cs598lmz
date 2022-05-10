import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)
import sys
import json
import os
import re
import datetime
import time
import requests
import urllib
import copy
from tqdm import tqdm
import pandas as pd
import numpy as np
import csv
import logging
import logging.config
import logging.handlers
import traceback
import threading
import multiprocessing

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from common import common
from common import configHttp

logging.config.fileConfig('../conf/logging.conf')
logger = logging.getLogger('root')

class Base():
    def __init__(self):
        self.conf=configHttp.ConfigHttp()
        self.headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)
