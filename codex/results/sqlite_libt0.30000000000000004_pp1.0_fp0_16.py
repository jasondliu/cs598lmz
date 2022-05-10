import ctypes
import ctypes.util
import threading
import sqlite3
import time
import sys
import os
import re
import subprocess
import signal
import traceback

class Db(object):
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = sqlite3.connect(self.db_file)
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS events (id INTEGER PRIMARY KEY, timestamp INTEGER, type TEXT, data BLOB)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS config (key TEXT PRIMARY KEY, value TEXT)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS status (key TEXT PRIMARY KEY, value TEXT)")
        self.conn.commit()

    def insert_event(self, type, data):
        self.cursor.execute("INSERT INTO events (timestamp, type, data) VALUES (?, ?, ?)", (int(time.time()), type, data))
        self.conn.
