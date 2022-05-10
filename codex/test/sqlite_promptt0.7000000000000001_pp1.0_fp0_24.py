import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:', timeout=5.0)

__all__ = [ 'connect', 'Connection', 'Cursor', 'Row', 'Binary' ]

try:
    from pysqlite2.pysqlite2 import *
except ImportError:
    pass

def connect(database, timeout=None):
    """Opens a connection to the SQLite database file *database*. You can
    use ":memory:" to open a database connection to a database that resides
    in RAM instead of on disk."""
    return Connection(database, timeout)

class Connection(object):
    def __init__(self, database, timeout=None):
        self.__db = None
        self.__thread_ident = None
        self.timeout = timeout
        self.__db_lock = threading.Lock()
        self.__connect(database)

    def __connect(self, database):
        self.__db_lock.acquire()
