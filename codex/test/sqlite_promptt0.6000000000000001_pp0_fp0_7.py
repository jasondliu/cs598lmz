import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() with autocommit=True
# The Python code is executed in a separate thread to ensure that
# the call to sqlite3.connect() does not block.
#
# This test script assumes that the SQLite library has been compiled
# with -DSQLITE_THREADSAFE=2.
#
# The test fails if the Python code blocks indefinitely in
# sqlite3.connect().
#
# This test was written to verify that the Python code does not
# block when the system is low on memory.

db_filename = 'test.db'
sqlite_lib = ctypes.util.find_library('sqlite3')

def main():
    if sqlite_lib is None:
        print('Could not find sqlite3 library')
        sys.exit(1)

    try:
        os.remove(db_filename)
    except OSError:
        pass

    sqlite3 = ctypes.CDLL(sqlite_lib)
    sqlite3.sqlite3_initialize()
    print('sqlite3_initialize() succeeded')

    # Create a
