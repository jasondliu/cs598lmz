import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:").execute("pragma journal_mode")

# TODO: Support insert by 300 tweets at once
# TODO: Add lock when insert tweets table.
# TODO: Make thread safe.
# TODO: Add exception handling.

# NOTE: If you use multithread mode(sqlite3 thread safe mod is on.),
#       you should add lock to database.
# REFERENCE:
#   https://docs.python.org/2/library/sqlite3.html#sqlite3.connect
#
#   SQLITE_THREADSAFE
#   The SQLite library can be safely used by multiple threads
#   provided that no single database connection is used simultaneously
#   in two or more threads.
#   If two or more threads try to use the same database connection at the same time then the behaviour is undefined.

