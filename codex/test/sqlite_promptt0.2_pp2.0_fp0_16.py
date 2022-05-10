import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memdb1?mode=memory&cache=shared', uri=True)

class Sqlite3(object):
    def __init__(self, db_file):
        self.db_file = db_file
        self.lock = threading.Lock()
        self.conn = sqlite3.connect(self.db_file, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

    def execute(self, sql, args=None):
        with self.lock:
            if args:
                self.cursor.execute(sql, args)
            else:
                self.cursor.execute(sql)
            self.conn.commit()

    def executemany(self, sql, args):
        with self.lock:
            self.cursor.executemany(sql, args)
            self.conn.commit()

    def fetchall(self):
        return self.cursor.fetchall()

