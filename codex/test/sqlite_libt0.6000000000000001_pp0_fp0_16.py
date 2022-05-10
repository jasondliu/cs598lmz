import ctypes
import ctypes.util
import threading
import sqlite3
import datetime
import time
import subprocess
import os
import sys
import socket
import logging
import os

class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self

class database:
    def __init__(self):
        self.conn = sqlite3.connect(os.path.dirname(os.path.realpath(__file__)) + "/db.sqlite3", check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS server(id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(255), ip VARCHAR(255), port INTEGER, status VARCHAR(255), timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
