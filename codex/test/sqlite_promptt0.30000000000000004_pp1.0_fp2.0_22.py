import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")
# Test sqlite3.connect("")

# Test sqlite3.connect(None)
# Test sqlite3.connect(None, uri=True)

# Test sqlite3.connect(":memory:", uri=True)
# Test sqlite3.connect("", uri=True)

# Test sqlite3.connect("file:test?mode=memory&cache=shared", uri=True)
# Test sqlite3.connect("file::memory:?cache=shared", uri=True)

# Test sqlite3.connect("file:test?mode=memory", uri=True)
# Test sqlite3.connect("file::memory:", uri=True)

# Test sqlite3.connect("file:test?mode=ro", uri=True)
# Test sqlite3.connect("file:test?mode=rw", uri=True)
# Test sqlite3.connect("file:test?mode=rwc", uri=True)

# Test sqlite3.connect("file:test?mode=ro&
