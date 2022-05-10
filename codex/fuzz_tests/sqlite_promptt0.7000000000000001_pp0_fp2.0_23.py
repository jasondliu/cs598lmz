import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() to make sure it is available
sqlite3.connect(':memory:')

# SQLite3 has no C API for getting the last inserted rowid. This is a workaround
# for that.
_last_inserted_rowid_lock = threading.Lock()
_last_inserted_rowid = None


def _sqlite3_callback(userdata, ncols, colvals, colnames):
    """
    Called by sqlite3.exec() to save the last inserted rowid.
    """
    global _last_inserted_rowid
    with _last_inserted_rowid_lock:
        _last_inserted_rowid = colvals[0]


def _sqlite3_get_last_inserted_rowid(conn):
    """
    ``conn`` is the SQLite3 connection object.
    """
    sql = "SELECT last_insert_rowid()"
    conn.exec_(sql, _sqlite3_callback, None)
    with _last_inserted_rowid_lock:
        return _last_inserted_row
