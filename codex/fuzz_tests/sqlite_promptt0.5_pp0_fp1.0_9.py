import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")

class SQLite3Wrapper(object):
    def __init__(self, database):
        self.database = database
        self.connection = None
        self.cursor = None
        self.lock = threading.Lock()
        self.connect()

    def connect(self):
        self.connection = sqlite3.connect(self.database)
        self.cursor = self.connection.cursor()

    def execute(self, query, args=None):
        self.lock.acquire()
        if self.connection is None:
            self.connect()
        if args is None:
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, args)
        self.lock.release()

    def executemany(self, query, args):
        self.lock.acquire()
        if self.connection is None:
            self.connect()
        self.cursor.executemany(query, args)
        self.lock.release()

    def commit(self):
        self.
