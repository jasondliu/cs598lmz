import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('test.db')

class _Cursor(object):
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()
        self.cursor.arraysize = 100

    def __getattr__(self, name):
        return getattr(self.cursor, name)

    def __iter__(self):
        return iter(self.cursor)

    def execute(self, sql, args=None):
        if args is None:
            args = []
        self.cursor.execute(sql, args)

    def executemany(self, sql, args):
        self.cursor.executemany(sql, args)

    def close(self):
        self.cursor.close()

    def commit(self):
        self.conn.commit()

    def rollback(self):
        self.conn.rollback()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

