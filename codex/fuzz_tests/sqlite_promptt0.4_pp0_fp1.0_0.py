import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")
#print(sqlite3.connect(":memory:"))
#print(sqlite3.connect(":memory:").cursor())

class Sqlite3(object):
    def __init__(self, path):
        self.path = path
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn = sqlite3.connect(self.path)
        self.cursor = self.conn.cursor()

    def close(self):
        self.conn.close()

    def execute(self, sql, *args):
        self.cursor.execute(sql, *args)

    def executemany(self, sql, *args):
        self.cursor.executemany(sql, *args)

    def commit(self):
        self.conn.commit()

    def fetchone(self):
        return self.cursor.fetchone()

    def fetchmany(self, size=None):
        return self.cursor.fetchmany(size)

    def fetchall(
