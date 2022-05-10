import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os

class Sqlite3Database(object):
    def __init__(self, filename):
        self.filename = filename
        self.db = sqlite3.connect(self.filename)
        self.db.text_factory = str
        self.cursor = self.db.cursor()
        self.cursor.execute("PRAGMA synchronous = OFF")
        self.cursor.execute("PRAGMA journal_mode = MEMORY")
        self.cursor.execute("PRAGMA locking_mode = EXCLUSIVE")
        self.cursor.execute("PRAGMA cache_size = 8192")
        self.cursor.execute("PRAGMA count_changes = OFF")
        self.cursor.execute("PRAGMA temp_store = MEMORY")
        self.cursor.execute("PRAGMA auto_vacuum = FULL")
        self.cursor.execute("PRAGMA foreign_keys = OFF")
        self.cursor.execute("PRAGMA page_size = 4096")
