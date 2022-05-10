import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

class Cursor(object):
    """
    A base class for cursors that wraps sqlite3 cursors.
    """
    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()
        self.lock = threading.Lock()

    def execute(self, query, args=()):
        self.lock.acquire()
        self.cursor.execute(query, args)
        self.lock.release()

    def executemany(self, query, args):
        self.lock.acquire()
        self.cursor.executemany(query, args)
        self.lock.release()

    def fetchone(self):
        return self.cursor.fetchone()

    def fetchall(self):
        return self.cursor.fetchall()

    def commit(self):
        self.connection.commit()

class Connection(object):
    """
    A base class for connections that wraps sqlite3 connections.
    """
