import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect with the uri of a file, and with a file:// uri.
conn = sqlite3.connect("test.db")
try:
    conn.text_factory = str
    cur = conn.cursor()
    cur.execute("select sqlite_version()")
    data = cur.fetchone()
    print("SQLite version: %s" % data)
finally:
    conn.close()

# Test sqlite3.connect with the uri of a file, and with a file:// uri.
conn = sqlite3.connect("file:test.db?mode=rw", uri=True)
try:
    conn.text_factory = str
    cur = conn.cursor()
    cur.execute("select sqlite_version()")
    data = cur.fetchone()
    print("SQLite version: %s" % data)
finally:
    conn.close()

# Test sqlite3.connect with the uri of a database that does not exist,
# and with a file:// uri.
conn = sqlite3.connect
