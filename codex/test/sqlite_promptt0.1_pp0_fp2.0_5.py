import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")

# Test sqlite3.connect("file:memdb1?mode=memory&cache=shared")

# Test sqlite3.connect("file::memory:?cache=shared")

# Test sqlite3.connect("file::memory:", uri=True)

# Test sqlite3.connect("file:memdb1?mode=memory", uri=True)

# Test sqlite3.connect("file::memory:", uri=True)

# Test sqlite3.connect("file::memory:?cache=shared", uri=True)

# Test sqlite3.connect(":memory:", uri=True)

# Test sqlite3.connect("file:memdb1?mode=memory&cache=shared", uri=True)

# Test sqlite3.connect("file::memory:?cache=shared", uri=True)

# Test sqlite3.connect(":memory:", check_same_thread=False)

# Test sqlite3.connect("file:memdb1?mode=memory&cache=shared",
