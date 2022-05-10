import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

connect_lock = threading.Lock()

def connect(database, timeout=10):
    connect_lock.acquire()
    try:
        conn = sqlite3.connect(database, timeout=timeout)
    finally:
        connect_lock.release()
    return conn

def connect_with_retry(database, timeout=10):
    # This is not thread safe.
    # But we're not running threads, so it's ok.
    for i in range(10):
        try:
            return connect(database, timeout=timeout)
        except sqlite3.OperationalError:
            pass
    raise sqlite3.OperationalError("Could not connect to database")

class Connection:
    def __init__(self, database, timeout=10):
        self.conn = connect_with_retry(database, timeout=timeout)
        self.cursor = self.conn.cursor()

    def execute(self, sql, *args, **kwargs):
        return self.cursor.execute(sql, *args, **kwargs)

