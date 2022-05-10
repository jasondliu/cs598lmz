import ctypes
import ctypes.util
import threading
import sqlite3
import pandas as pd
from pathlib import Path
import psutil
import sys
from sys import platform
import os
import time
from datetime import datetime, timedelta
from dateutil import tz
from dateutil.parser import parse
from dateutil.tz import tzlocal
from timeit import default_timer as timer
from time import sleep
import logging
from logging.handlers import TimedRotatingFileHandler
from logging.handlers import SMTPHandler
from logging import StreamHandler
from logging import FileHandler
import unittest

# from project_funcs import *
from config import *
from rsid_parser import *
from vcf_parser import *
from db_update import *
from logger_info import *


def timestamp():
    ts = time.time()
    st = datetime.fromtimestamp(ts).strftime('[%Y-%m-%d %H:%M:%S]')
    return st


def check_missing_snps(rsid_objects):
    """Checks if (1) any RSIDs in the list are missing from the
