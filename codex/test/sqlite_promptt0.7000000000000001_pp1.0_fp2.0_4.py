import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() in the same way as sqlite3.Connection(),
# but don't expose the Connection object.
def connect(database, timeout=5.0, detect_types=0, isolation_level=None,
            check_same_thread=False, factory=None, cached_statements=100, uri=False):
    """Opens a connection to the SQLite database file *database*. You can use
    ":memory:" to open a database connection to a database that resides in
    RAM instead of on disk.
    """
    # TODO: when timeout is not None, set it only if it's not already set
    def _connect(database, timeout, detect_types, isolation_level,
                 check_same_thread, factory, cached_statements):
        try:
            return Connection(database, timeout, detect_types,
                              isolation_level, check_same_thread, factory,
                              cached_statements, uri)
        except OperationalError as e:
            raise e # FIXME: not that pretty
