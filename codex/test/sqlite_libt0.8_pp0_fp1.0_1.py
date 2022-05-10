import ctypes
import ctypes.util
import threading
import sqlite3
import datetime
import os


class RoamDB(object):

    def __init__(self, database_file):
        self.database_file = database_file

    def __enter__(self):
        self.lock = threading.Lock()
        conn = sqlite3.connect(self.database_file, timeout=60.0)

        # Create tables if they are missing
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS wifi
            (
                "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                "ssid" TEXT NOT NULL,
                "bssid" TEXT NOT NULL,
                "last_seen" DATETIME NOT NULL
            )
            ''')
