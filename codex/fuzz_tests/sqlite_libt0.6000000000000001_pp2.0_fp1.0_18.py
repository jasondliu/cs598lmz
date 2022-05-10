import ctypes
import ctypes.util
import threading
import sqlite3
import binascii
import datetime
import os
import sys
import queue
import time

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter
import matplotlib.ticker as ticker


class Database:
    def __init__(self, file=None):
        if file is None:
            self.db = sqlite3.connect(":memory:")
        else:
            self.db = sqlite3.connect(file)
        self.cursor = self.db.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS data
                               (timestamp DATETIME NOT NULL,
                                data BLOB NOT NULL)""")

    def insert(self, data):
        self.cursor.execute("INSERT INTO data VALUES (?, ?)",
                            (datetime.datetime.now(), data))
        self.db.commit()

    def get(self, start=None, end=None):
        if start is None and end is
