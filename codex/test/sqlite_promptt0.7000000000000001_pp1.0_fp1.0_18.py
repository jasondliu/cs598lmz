import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect().
conn = sqlite3.connect(":memory:")
cur = conn.cursor()
cur.execute('SELECT SQLITE_VERSION()')
