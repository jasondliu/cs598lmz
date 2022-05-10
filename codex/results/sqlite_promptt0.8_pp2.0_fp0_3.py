import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')
import time

# Python < 3.2 compatibility
try:
    xrange
except NameError:
    xrange = range

class Sqlite3LockTest(unittest.TestCase):
    def setUp(self):
        # Determine if we can lock the database. This should work on
        # most Unix platforms.
        try:
            dll = ctypes.CDLL(ctypes.util.find_library('c'), use_errno=True)
            self.flock = dll.flock
            self.flock.argtypes = [ctypes.c_int, ctypes.c_int]
        except:
            self.flock = None
        self.lockfile = 'sqlite3.db-journal'
        self.lockfd = None
        self.lockthreads = []
        self.lockdb = sqlite3.connect(':memory:')
        self.lockdb.execute('create table locktable (foo integer)')
        self.lockdb.execute('insert into locktable values (1)')
        self.
