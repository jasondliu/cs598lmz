import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")

class Sqlite3:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()
        self.lock = threading.Lock()

    def __del__(self):
        self.close()

    def close(self):
        self.conn.close()

    def execute(self, sql, param=None):
        self.lock.acquire()
        try:
            if param:
                self.cursor.execute(sql, param)
            else:
                self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            print >> sys.stderr, e
        finally:
            self.lock.release()

    def select(self, sql, param=None):
        self.lock.acquire()
