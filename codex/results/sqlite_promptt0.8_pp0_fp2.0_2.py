import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
conn = sqlite3.connect(":memory:")

# This is a normal connection object.
print(conn.__class__)

# It has a cursor, which provides a way to run queries
print(conn.cursor().__class__)

# Execute queries fast
cur = conn.cursor()
cur.execute("create table test(x integer);")
cur.execute("insert into test (x) values (1);")
cur.execute("insert into test (x) values (2);")
cur.execute("insert into test (x) values (3);")

# Selects all rows
cur.execute("select x from test;")
results = cur.fetchall()
print(results)

# SQLite also provides a convenience function for closing.
# If you don't close, you will experience weird cursors
conn.close()

# But in Python, you don't have to use sqlite_close()
# Python will destroy the object and its underlying connection
# at the end of the 'with' block
with sqlite3.connect(":memory:") as conn:

