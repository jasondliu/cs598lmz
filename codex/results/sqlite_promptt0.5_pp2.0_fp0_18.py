import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared')

class _SQLiteObject(object):
    """
    Base class for the shared SQLite connection.
    """
    def __init__(self, database, timeout=5.0, isolation_level=None,
                 check_same_thread=True, factory=None, cached_statements=100):
        # Create a single shared connection and cursor.
        self.database = database
        self.timeout = timeout
        self.isolation_level = isolation_level
        self.check_same_thread = check_same_thread
        self.factory = factory
        self.cached_statements = cached_statements
        self._connection_lock = threading.Lock()
        self._sqlite_lock = threading.Lock()
        self._connection = None
        self._db_mutex = None
        self._closed = False
        self._row_factory = None
        self._dirty = False
        self._conn_kwargs = {
            'database': self.database,
            'timeout': self.timeout,
            'is
