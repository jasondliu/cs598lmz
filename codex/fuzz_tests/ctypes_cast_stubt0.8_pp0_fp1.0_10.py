import ctypes
ctypes.cast(None, ctypes.py_object)

import os
import sys
import pymongo
import datetime
import json
from multiprocessing import Process, Manager, Value, Lock
import time
import math
import numpy as np

# import common package in parent directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))

import mongodb_client

NEWS_TABLE_NAME = "news"

NUM_OF_CLASS = 17

SCRAPPER_NEWS_QUEUE_TABLE_NAME = "scrapper_news_queue"

SLEEP_TIME_IN_SECONDS = 1

def run(skip, url, batch_size, db, total_news_num, candidate_model_list, 
    total_news_processed, start_time, process_index):
    # skip = 0
    # batch_size = 10
    while True:
        # Get the ids from queue
        news = db[SCRAPPER_NEWS_QUEUE_TABLE
