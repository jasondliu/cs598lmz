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
    try:
        conn = sqlite3.connect(db, check_same_thread = False)
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY AUTOINCREMENT, val text);")
        c.execute("INSERT INTO test (val) VALUES ('test');")
        c.execute("SELECT * FROM test;")
        row = c.fetchone()
        if row:
            logger.info("sqlite3 connection OK")
            return True

