import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("example.db")
# Test sqlite3.connect("/root/sqlite/test.db")
# Test sqlite3.connect("/root/sqlite/test.db", uri=True)
# Test sqlite3.connect("file:/root/sqlite/test.db")
# Test sqlite3.connect("file:/root/sqlite/test.db", uri=True)
# Test sqlite3.connect("file:/root/sqlite/test.db?mode=ro", uri=True)
# Test sqlite3.connect("file:/root/sqlite/test.db?mode=rw", uri=True)
# Test sqlite3.connect("file:/root/sqlite/test.db?mode=rwc", uri=True)
# Test sqlite3.connect(":memory:")
# Test sqlite3.connect(":memory:", uri=True)
# Test sqlite3.connect("file:test.db?mode=rwc", uri=True)
# Test sqlite3.connect("file::memory:?cache=shared",
