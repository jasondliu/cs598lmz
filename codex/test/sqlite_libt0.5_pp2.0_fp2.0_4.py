import ctypes
import ctypes.util
import threading
import sqlite3

#-------------------------------------------------------------------------------
#
#-------------------------------------------------------------------------------

class libc:
    def __init__(self):
        self.libc = ctypes.CDLL(ctypes.util.find_library('c'))
    def sched_yield(self):
        self.libc.sched_yield()

#-------------------------------------------------------------------------------
#
#-------------------------------------------------------------------------------

class sqlite:

    def __init__(self, database):
        self.conn = sqlite3.connect(database, check_same_thread = False)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()
        self.cursor.execute('PRAGMA synchronous = OFF')
        self.cursor.execute('PRAGMA journal_mode = MEMORY')

    def execute(self, *args):
        self.cursor.execute(*args)

    def executemany(self, *args):
        self.cursor.executemany(*args)

    def commit(self):
        self.conn.commit()

