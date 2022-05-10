import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")
# Test sqlite3.connect("/tmp/test.db")
# Test sqlite3.connect("file::memory:?cache=shared")

# Test sqlite3.connect("file::memory:?cache=shared", uri=True)
# Test sqlite3.connect("file::memory:?cache=shared", uri=False)
# Test sqlite3.connect("file::memory:?cache=shared", uri=None)

# Test sqlite3.connect("file::memory:?cache=shared", uri=True, detect_types=sqlite3.PARSE_DECLTYPES)
# Test sqlite3.connect("file::memory:?cache=shared", uri=False, detect_types=sqlite3.PARSE_DECLTYPES)
# Test sqlite3.connect("file::memory:?cache=shared", uri=None, detect_types=sqlite3.PARSE_DECLTYPES)

# Test sqlite3.connect("file::memory:?cache=shared", uri=True, detect
