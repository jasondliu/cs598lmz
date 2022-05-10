import ctypes
import ctypes.util
import threading
import sqlite3
import sys

class SqliteError(Exception):
    pass

class SqliteLockError(Exception):
    pass

class Sqlite:
    def __init__(self, filename):
        self.filename = filename
        self.connection = None
        self.lock_file = None

    def __enter__(self):
        self.lock()
        self.connection = sqlite3.connect(self.filename)
        return self.connection

    def __exit__(self, type, value, traceback):
        self.connection.close()
        self.unlock()

    def lock(self):
        lock_file_name = self.filename + '.lock'
        if os.path.exists(lock_file_name):
            raise SqliteLockError('Database already locked: %s' % lock_file_name)

        self.lock_file = open(lock_file_name, 'w')
        fcntl = ctypes.CDLL(ctypes.util.find_library('c'))
