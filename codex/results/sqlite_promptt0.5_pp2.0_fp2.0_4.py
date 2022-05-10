import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

class Db(object):
    def __init__(self, name):
        self.name = name
        self.conn = sqlite3.connect(name)
        self.cursor = self.conn.cursor()

    def execute(self, query):
        self.cursor.execute(query)

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()

class DbLock(object):
    def __init__(self, name):
        self.name = name
        self.lock = threading.Lock()
        self.db = Db(name)

    def __enter__(self):
        self.lock.acquire()
        return self.db

    def __exit__(self, type, value, traceback):
        self.db.close()
        self.lock.release()


def create_table(db):
    db.execute('''CREATE TABLE IF NOT EXISTS
                  users(id INTEGER PRIMARY KEY AUTOINCRE
