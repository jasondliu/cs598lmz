import ctypes
import ctypes.util
import threading
import sqlite3

class Database(object):
    def __init__(self, db_path):
        self.db_lock = threading.Lock()
        self.db_path = db_path
        self.db_connection = None
        self.db_cursor = None

    def __del__(self):
        self.db_lock.acquire()
        if self.db_connection is not None:
            self.db_connection.close()
        self.db_lock.release()

    def _open_database(self):
        if self.db_connection is None:
            self.db_connection = sqlite3.connect(self.db_path, check_same_thread=False)
            self.db_cursor = self.db_connection.cursor()
            self.db_cursor.execute("PRAGMA foreign_keys = ON;")
            self.db_connection.commit()

    def execute(self, *args):
        self.db_lock.acquire()
        self._open_database()
        self.db_cursor.execute(*args)
