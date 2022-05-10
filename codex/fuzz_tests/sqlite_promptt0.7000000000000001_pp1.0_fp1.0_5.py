import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect


class SQLite3Connector(object):
    def __init__(self, dbfile, table):
        self.dbfile = dbfile
        self.table = table

    def __enter__(self):
        self.conn = sqlite3.connect(self.dbfile)
        return self.conn

    def __exit__(self, type, value, traceback):
        self.conn.close()


class SQLite3Cursor(object):
    def __init__(self, dbfile, table):
        self.dbfile = dbfile
        self.table = table

    def __enter__(self):
        self.conn = sqlite3.connect(self.dbfile)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, type, value, traceback):
        self.cursor.close()
        self.conn.close()


class SQLite3Thread(threading.Thread):
    def __init__(self, dbfile, table):
        threading.Thread.__init__(
