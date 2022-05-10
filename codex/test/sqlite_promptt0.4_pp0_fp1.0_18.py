import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

class Sqlite3:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.lock = threading.Lock()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def execute(self, sql, *args):
        self.lock.acquire()
        try:
            self.cursor.execute(sql, args)
            self.conn.commit()
        except sqlite3.Error as e:
            print(e)
            self.conn.rollback()
        self.lock.release()

    def executemany(self, sql, *args):
        self.lock.acquire()
        try:
            self.cursor.executemany(sql, args)
            self.conn.commit()
        except sqlite3.Error as e:
            print(e)
            self
