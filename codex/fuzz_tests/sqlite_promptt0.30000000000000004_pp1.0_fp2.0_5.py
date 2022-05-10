import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

class Db(object):
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self.conn.text_factory = str
        self.cursor = self.conn.cursor()
        self.lock = threading.Lock()

    def __del__(self):
        self.conn.close()

    def execute(self, sql, *args):
        self.lock.acquire()
        try:
            self.cursor.execute(sql, args)
            self.conn.commit()
        except Exception as e:
            print e
        finally:
            self.lock.release()

    def executemany(self, sql, *args):
        self.lock.acquire()
        try:
            self.cursor.executemany(sql, args)
            self.conn.commit()
        except Exception as e:
            print e
        finally:
            self.lock.release()

    def fetchall
