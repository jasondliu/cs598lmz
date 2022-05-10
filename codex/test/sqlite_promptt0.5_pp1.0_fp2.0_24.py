import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:").execute("select 1").fetchall()

# TODO: use sqlite3.Row to get case-insensitive column names

class SQLite:
    def __init__(self, filename):
        self.filename = filename
        self.connection = sqlite3.connect(filename)
        self.connection.text_factory = str
        self.connection.row_factory = sqlite3.Row
        self.connection.execute("PRAGMA foreign_keys = ON")
        self.connection.execute("PRAGMA journal_mode = WAL")
        self.connection.execute("PRAGMA synchronous = OFF")
        self.connection.isolation_level = None
        self.cursor = self.connection.cursor()
        self.lock = threading.Lock()

    def execute(self, *args):
        with self.lock:
            self.cursor.execute(*args)

    def fetchone(self):
        with self.lock:
            return self.cursor.fetchone()

