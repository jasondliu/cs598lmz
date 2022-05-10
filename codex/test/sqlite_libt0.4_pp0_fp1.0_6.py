import ctypes
import ctypes.util
import threading
import sqlite3
import logging
import time
import os
import sys
import traceback

logger = logging.getLogger('sqlite3')

class SQLite3(object):
    def __init__(self, db_file):
        self.db_file = db_file
        self.db = None
        self.lock = threading.Lock()
        self.connect()
        self.init_database()

    def connect(self):
        self.db = sqlite3.connect(self.db_file, check_same_thread=False)
        self.db.text_factory = str
        self.db.row_factory = sqlite3.Row

    def init_database(self):
        with self.db:
            c = self.db.cursor()
            c.execute("CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT, `username` TEXT NOT NULL UNIQUE, `password` TEXT NOT NULL)")
