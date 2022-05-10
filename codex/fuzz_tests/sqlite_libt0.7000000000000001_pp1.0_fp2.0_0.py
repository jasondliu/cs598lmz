import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os
import sys
import re
import errno

class Database(object):
    """
    An SQLite3 database for storing user-specific metadata.
    """
    def __init__(self, path):
        self.path = path
        self.connection = None
        self.transaction_depth = 0
        self.thread_ident = 0
        self.lock = threading.Lock()

    def __enter__(self):
        if not self.connection:
            self.connection = sqlite3.connect(self.path)
            self.connection.isolation_level = None
        else:
            raise Exception("Connection is already active")

        self.thread_ident = threading.current_thread().ident
        self.lock.acquire()
        return self

    def __exit__(self, type, value, traceback):
        self.lock.release()
        self.thread_ident = 0
        self.connection.close()
        self.connection = None

    def execute(self, sql, args=None):
        """
        Execute an
