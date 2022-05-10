import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")

sqlite3.connect(":memory:")

# Test sqlite3.connect(":memory:")

# Test sqlite3.connect("")

try:
    sqlite3.connect("")
except sqlite3.OperationalError:
    pass

# Test sqlite3.connect("")

# Test sqlite3.connect("file::memory:")

try:
    sqlite3.connect("file::memory:")
except sqlite3.OperationalError:
    pass

# Test sqlite3.connect("file::memory:")

# Test sqlite3.connect("file::memory:?cache=shared")

try:
    sqlite3.connect("file::memory:?cache=shared")
except sqlite3.OperationalError:
    pass

# Test sqlite3.connect("file::memory:?cache=shared")

# Test sqlite3.connect(":memory:", uri=True)

