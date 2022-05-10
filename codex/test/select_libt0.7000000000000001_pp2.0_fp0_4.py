import select_data
import sys
import os
import gc
import re
import time
import datetime
import threading
#from threading import Thread
import mysql.connector
from mysql.connector import errorcode
import logging

def read_log_config():
    logging.config.fileConfig("logging.conf")
    logger = logging.getLogger("main")
    return logger

logger = read_log_config()

def get_date_time():
    now = datetime.datetime.now()
    date_time = str(now.year) + "-" + str(now.month) + "-" + str(now.day) + " " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
