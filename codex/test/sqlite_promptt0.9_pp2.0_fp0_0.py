import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connections for cursors that never die

THREADS = 2
CONNECTIONS = 100
NUM_OPERATIONS = 100

# Let each thread try to open a new database connection
# and perform some dummy operations on it.
# If a thread finds a connection whose cursor is still alive,
# complain.

def worker(i):
    for j in range(NUM_OPERATIONS):
        conn = sqlite3.connect(":memory:")
        cursor = conn.cursor()
        if not cursor.close:
            raise RuntimeError("cursor.close does not exist")
        if cursor.closed:
            raise RuntimeError("cursor.closed is present")
        if cursor() is not cursor:
            raise RuntimeError("cursor is not a callable")
        if cursor.fetchone is not sqlite3.Cursor.fetchone:
            raise RuntimeError("cursor.fetchone is not the base method")
        if "fetchone" in dir(cursor):
            raise RuntimeError("cursor.fetchone is in dir()")
        # Check that the cursor can execute a
