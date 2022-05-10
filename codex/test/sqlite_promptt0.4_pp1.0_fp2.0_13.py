import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

class sqlite3_connection(sqlite3.Connection):
    def __init__(self, *args, **kwargs):
        sqlite3.Connection.__init__(self, *args, **kwargs)
        self.isolation_level = None
        self.connection_lock = threading.Lock()

    def _begin(self):
        self.isolation_level = 'IMMEDIATE'
        self.execute('BEGIN %s' % self.isolation_level)

    def _commit(self):
        self.execute('COMMIT')
        self.isolation_level = None

    def _rollback(self):
        self.execute('ROLLBACK')
        self.isolation_level = None

    def commit(self):
        with self.connection_lock:
            if self.isolation_level is not None:
                self._commit()

    def rollback(self):
        with self.connection_lock:
            if self.isolation_level is not None:
                self._rollback()

