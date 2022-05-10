import ctypes
import ctypes.util
import threading
import sqlite3
import time
import signal
import os
import sys
import ast

# import the Django settings file
sys.path.append(os.getcwd())
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
import settings

class Profile(object):
    def __init__(self, conn):
        self.conn = conn
        # create the database tables if they don't exist
        self.create_tables()

    def create_tables(self):
        """Create database tables."""
        sql = """CREATE TABLE IF NOT EXISTS profile (
            id INTEGER PRIMARY KEY,
            started TEXT,
            ended TEXT,
            thread TEXT,
            filename TEXT,
            lineno INTEGER,
            fullname TEXT,
            funcname TEXT,
            count INTEGER,
            total_time TEXT
        )"""
        self.conn.execute(sql)
        self.conn.commit()

    def add_profile(self, profile_info):
        """Add a profile item."""
        # SQLite doesn't know
