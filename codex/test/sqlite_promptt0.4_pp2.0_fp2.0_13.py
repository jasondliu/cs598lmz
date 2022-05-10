import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memdb1?mode=memory&cache=shared', uri=True)

import logging
logging.basicConfig(level=logging.DEBUG)

#import pdb
#pdb.set_trace()

class SQLite3(object):
    def __init__(self, db_filename):
        self.db_filename = db_filename
        self.lock = threading.Lock()
        self.conn = None

    def __enter__(self):
        self.lock.acquire()
        self.conn = sqlite3.connect(self.db_filename)
        return self.conn

    def __exit__(self, type, value, traceback):
        self.conn.commit()
        self.conn.close()
        self.lock.release()

class SQLite3_shared_cache(object):
    def __init__(self, db_filename):
        self.db_filename = db_filename
        self.lock = threading.Lock()
        self.conn = None

    def __enter__(self):
        self.lock
