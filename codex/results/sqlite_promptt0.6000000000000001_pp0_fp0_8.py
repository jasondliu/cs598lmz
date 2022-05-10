import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
# Test sqlite3.connect(":memory:")

# Test sqlite3.connect("db.sqlite")
# Test sqlite3.connect("db.sqlite3")
# Test sqlite3.connect("db.db")
# Test sqlite3.connect("/tmp/db.sqlite")
# Test sqlite3.connect("/tmp/db.db")
# Test sqlite3.connect("/tmp/db.sqlite3")

# Test sqlite3.connect("/tmp/db.sqlite", uri=True)
# Test sqlite3.connect("file:/tmp/db.sqlite", uri=True)
# Test sqlite3.connect("file:///tmp/db.sqlite", uri=True)
# Test sqlite3.connect("file://localhost/tmp/db.sqlite", uri=True)

# Test sqlite3.connect("/tmp/db.db", uri=True)
# Test sqlite3.connect("file:/tmp/db.db", uri=True)
# Test sqlite3.connect("
