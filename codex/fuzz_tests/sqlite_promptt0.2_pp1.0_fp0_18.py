import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

class Sqlite3(object):
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.lock = threading.Lock()

    def __del__(self):
        self.conn.close()

    def execute(self, sql):
        self.lock.acquire()
        self.cursor.execute(sql)
        self.lock.release()

    def executemany(self, sql, params):
        self.lock.acquire()
        self.cursor.executemany(sql, params)
        self.lock.release()

    def commit(self):
        self.lock.acquire()
        self.conn.commit()
        self.lock.release()

    def fetchall(self):
        self.lock.acquire()
        result = self.cursor.fetchall()
        self.lock.release()
        return result


