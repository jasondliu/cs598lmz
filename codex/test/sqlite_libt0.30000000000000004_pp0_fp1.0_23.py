import ctypes
import ctypes.util
import threading
import sqlite3
import time
import sys

class DbThread(threading.Thread):
    def __init__(self, db_name):
        threading.Thread.__init__(self)
        self.db_name = db_name
        self.db_conn = sqlite3.connect(db_name)
        self.db_cursor = self.db_conn.cursor()
        self.db_cursor.execute("CREATE TABLE IF NOT EXISTS data (time INTEGER, value REAL)")
        self.db_conn.commit()
        self.db_cursor.execute("CREATE TABLE IF NOT EXISTS config (key TEXT, value TEXT)")
        self.db_conn.commit()
        self.db_cursor.execute("SELECT value FROM config WHERE key = 'last_time'")
        self.last_time = self.db_cursor.fetchone()
        if self.last_time is None:
            self.last_time = 0
        else:
            self.last_time = int(self.last_time[0])

