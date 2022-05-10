import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connection.cursor()

try:
    import sqlite3
except ImportError:
    import sqlite as sqlite3

con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.execute("create table test (i)")

c1 = con.cursor()
c2 = con.cursor()
c1.execute("insert into test values (1)")
c2.execute("insert into test values (2)")
c1.execute("select * from test")
c2.execute("select * from test")
print(c1.fetchall())
print(c2.fetchall())

cur.execute("select * from test")
print(cur.fetchall())

# Test sqlite3.connection.total_changes

try:
    import sqlite3
except ImportError:
    import sqlite as sqlite3

con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.execute("create table test (i)")
cur.execute("insert into test values (1)")
