import ctypes
import ctypes.util
import threading
import sqlite3
import Queue
import contextlib


def connect(fn):
    def wrapped(self, *args, **kwargs):
        with contextlib.closing(sqlite3.connect(self.dbpath)) as conn:
            conn.row_factory = self._row_factory
            return fn(self, conn, *args, **kwargs)
    return wrapped


class Db(object):
    def __init__(self, dbpath):
        self.dbpath = dbpath
        self._row_factory = sqlite3.Row
        self._configure()

    def close(self):
        pass

    @connect
    def set(self, conn, key, value):
        sql = 'INSERT OR REPLACE INTO config VALUES (?, ?)'
        conn.execute(sql, (key, value))

    @connect
    def get(self, conn, key, default=None):
        sql = 'SELECT value FROM config WHERE key = ? LIMIT 1'
        results = conn.execute(sql, (key,)).fetchall()
