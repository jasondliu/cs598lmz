import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

class _sqlite3_connection(object):
    def __init__(self, db):
        self._db = db

    def cursor(self):
        return _sqlite3_cursor(self._db)

    def commit(self):
        pass

    def close(self):
        pass

class _sqlite3_cursor(object):
    def __init__(self, db):
        self._db = db

    def execute(self, query):
        self._db.execute(query)

    def fetchall(self):
        return self._db.fetchall()

    def fetchone(self):
        return self._db.fetchone()

    def close(self):
        pass

class _sqlite3_database(object):
    def __init__(self, db):
        self._db = db

    def execute(self, query):
        self._db.execute(query)

    def fetchall(self):
        return self._db.fetchall()

    def fetchone(self):
        return self
