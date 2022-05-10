import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("/tmp/test.db", check_same_thread = False)

import queue
import time

import logging
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
logger = logging.getLogger(__name__)


def test_sqlite3_connection(db):
    logger.info("testing sqlite3 connection to %s" % (db))
