import ctypes
import ctypes.util
import threading
import sqlite3
import os
import time
import json
import sys
import subprocess
import signal
import logging

from . import lib

class Db(object):
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS hosts (
                host TEXT PRIMARY KEY,
                last_seen INTEGER,
                last_seen_ip TEXT
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS dns (
                host TEXT,
                ip TEXT,
                timestamp INTEGER
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS arp (
                ip TEXT,
                mac TEXT,
                timestamp INTEGER
            )

