import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")

class DummyConnection(object):

    def __init__(self, cursor_factory):
        self.cursor_factory = cursor_factory
        self.open = True
        self.closed = False
        self.initial_isolation_level = None
        self.isolation_level = None

    def cursor(self):
        return self.cursor_factory()

    def close(self):
        self.open = False
        self.closed = True

    def commit(self):
        pass

    def rollback(self):
        pass

    def set_isolation_level(self, level):
        self.isolation_level = level
        if self.initial_isolation_level is None:
            self.initial_isolation_level = level

    def get_isolation_level(self):
        return self.isolation_level

class DummyCursor(object):

    def __init__(self):
        self.executed = None

    def execute(self, sql, parameters=None):
        self.executed
