import ctypes
import ctypes.util
import threading
import sqlite3
import datetime
import os
import sys

# libc = ctypes.CDLL(ctypes.util.find_library('c'))

class User(object):
    def __init__(self, username, password, ip):
        self.username = username
        self.password = password
        self.ip = ip
        self.logged_in = False
        self.logged_out = False
        self.last_seen = datetime.datetime.now()

class UserDB(object):
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = None
        self.cur = None

    def connect(self):
        self.conn = sqlite3.connect(self.db_path, check_same_thread=False)
        self.cur = self.conn.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS users(
            ip TEXT,
            username TEXT,
            password TEXT,
            logged_in INTEGER,
            logged_out INT
