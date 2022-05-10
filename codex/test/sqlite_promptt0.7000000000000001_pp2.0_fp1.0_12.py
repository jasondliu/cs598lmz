import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
conn = sqlite3.connect(":memory:")
cur = conn.cursor()
cur.execute("create table data(x integer)")
cur.execute("insert into data values (1)")
# We can read it back in Python
cur.execute("select x from data")
