import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

class Sqlite3(object):
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = sqlite3.connect(self.db_file)
        self.conn.text_factory = str
        self.cursor = self.conn.cursor()
        self.lock = threading.Lock()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def execute(self, sql, args=None):
        self.lock.acquire()
