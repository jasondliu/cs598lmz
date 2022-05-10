import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")

class SQLite3(object):
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = sqlite3.connect(self.db_file)
        self.cursor = self.conn.cursor()
        self.lock = threading.Lock()

    def close(self):
        self.conn.close()

    def execute(self, sql):
        self.lock.acquire()
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        finally:
            self.lock.release()

    def executemany(self, sql, args):
        self.lock.acquire()
        try:
            self.cursor.executemany(sql, args)
            self.conn.commit()
        finally:
            self.lock.release()

    def query(self, sql):
        self.lock.acquire()
        try:
            self.cursor.execute(sql)
            return self.cursor.fetchall
