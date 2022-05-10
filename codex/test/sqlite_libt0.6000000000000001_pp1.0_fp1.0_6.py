import ctypes
import ctypes.util
import threading
import sqlite3
import json
import re
import os
import sys
import time
import datetime

from . import config

log = logging.getLogger(__name__)

class SqliteDatabase(object):
    def __init__(self, dbname):
        self.dbname = dbname
        self.db = sqlite3.connect(dbname, check_same_thread=False)
        self.db.text_factory = str

        # check whether the database is initialized
        self.cursor = self.db.cursor()
        self.cursor.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='config'")
        if self.cursor.fetchone()[0] == 0:
            self.initialize()

    def initialize(self):
        log.info("Initializing database %s", self.dbname)
        self.cursor.execute("""CREATE TABLE config
                (key TEXT PRIMARY KEY, value TEXT)""")
