import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import time
import datetime
import hashlib
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )

class SQLiteHandler(logging.Handler):
    def __init__(self, filename):
        logging.Handler.__init__(self)
        self.filename = filename
        self.db = sqlite3.connect(filename)
        self.cur = self.db.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS logs
            (date text, log text)''')

    def emit(self, record):
        self.cur.execute("INSERT INTO logs VALUES(?, ?)",
            (record.created, record.msg))
        self.db.commit()

    def close(self):
        self.db.close()
        logging.Handler.close(self)

