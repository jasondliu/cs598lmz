import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
conn = sqlite3.connect(":memory:")

# Test sqlite3.connect data type
if (type(conn) is not sqlite3.Connection):
  raise "expected Connection"

# Test sqlite3.Connection.commit
conn.commit()

# Test Connection.close
conn.close()

# Test Connection.cursor
cur = conn.cursor()

if (type(cur) is not sqlite3.Cursor):
  raise "expected Cursor"

cur.close()

conn.close()
conn = sqlite3.connect(":memory:")
cur = conn.cursor()

cur.execute("create table test (column);")

cur.close()
conn.close()

print 'All tests OK'
