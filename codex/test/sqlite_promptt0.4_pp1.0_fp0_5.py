import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")
# Test sqlite3.connect("file:memdb1?mode=memory&cache=shared")
# Test sqlite3.connect("file::memory:?cache=shared")
# Test sqlite3.connect("file:memdb2?mode=memory")
# Test sqlite3.connect("file::memory:")

# Test sqlite3.connect("file:memdb3?mode=memory&cache=shared", uri=True)
# Test sqlite3.connect("file:memdb4?mode=memory", uri=True)

# Test sqlite3.connect("file:memdb5?mode=memory&cache=shared", uri=True,
#                      check_same_thread=False)
# Test sqlite3.connect("file:memdb6?mode=memory", uri=True,
#                      check_same_thread=False)

# Test sqlite3.connect("file:memdb7?mode=memory&cache=shared", uri=True,
#                      check_same_thread=False, isolation_level=None)
#
