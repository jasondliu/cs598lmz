import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
# Test sqlite3.connect(":memory:")
# Test sqlite3.connect("")
# Test sqlite3.connect("file:")
# Test sqlite3.connect("file:test")
# Test sqlite3.connect("file:test?mode=ro")
# Test sqlite3.connect("file:test?mode=rw")
# Test sqlite3.connect("file:test?mode=rwc")
# Test sqlite3.connect("file:test?mode=memory")
# Test sqlite3.connect("file:test?mode=memory&cache=shared")
# Test sqlite3.connect("file::memory:")
# Test sqlite3.connect("file::memory:?cache=shared")
# Test sqlite3.connect("file:test?mode=memory&cache=shared", uri=True)
# Test sqlite3.connect("file::memory:?cache=shared", uri=True)
# Test sqlite3.connect("file:test?mode=memory", uri=True)
# Test sqlite3.connect("file::memory:
