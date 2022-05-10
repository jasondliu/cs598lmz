import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os
import sys

# ----------------------------------------------------------------------

class Db(object):

    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute("PRAGMA journal_mode=WAL")
        self.cursor.execute("PRAGMA synchronous=NORMAL")
        self.cursor.execute("PRAGMA cache_size=10000")
        self.cursor.execute("PRAGMA temp_store=MEMORY")
        self.cursor.execute("PRAGMA foreign_keys=ON")
        self.cursor.execute("PRAGMA encoding='UTF-8'")
        self.cursor.execute("PRAGMA page_size=4096")
        self.cursor.execute("PRAGMA locking_mode=EXCLUSIVE")
        self.cursor.execute("PRAGMA secure_delete=ON")
        self.cursor.execute
