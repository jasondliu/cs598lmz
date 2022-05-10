import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

class test_sqlite3(object):

    def __init__(self):
        self.lock = threading.Lock()
        self.db = sqlite3.connect(":memory:", check_same_thread=False)
        self.db.row_factory = sqlite3.Row

        self.db.execute("CREATE TABLE test (id INTEGER PRIMARY KEY, value TEXT)")
        self.db.execute("INSERT INTO test VALUES (NULL, 'test')")
        self.db.commit()

    def get_value(self):
        self.lock.acquire()
        self.db.execute("SELECT * FROM test")
        row = self.db.fetchone()
        self.lock.release()
        return row


def test_threads():
    t = test_sqlite3()

    def run():
        while True:
            row = t.get_value()
