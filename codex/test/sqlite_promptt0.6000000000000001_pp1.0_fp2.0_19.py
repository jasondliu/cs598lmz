import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connections

class Dummy_Connection(object):
    def __init__(self):
        self.rowcount = 0
        self.description = None
        self.closed = False
        self.arraysize = 1
        self.lastrowid = None

    def close(self):
        self.closed = True

    def commit(self):
        pass

    def rollback(self):
        pass

    def cursor(self):
        return Dummy_Cursor(self)

class Dummy_Cursor(object):
    def __init__(self, connection):
        self.connection = connection

    def close(self):
        pass

    def execute(self, sql, parameters=()):
        pass

    def executemany(self, sql, seq_of_parameters):
        pass

    def executescript(self, sql_script):
        pass

    def fetchone(self):
        return None

    def fetchmany(self, size=None):
        return ()

    def fetchall(self):
        return ()

