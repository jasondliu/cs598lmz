import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")


sqlite3.sqlite_version
sqlite3.sqlite_version_info


con = sqlite3.connect(":memory:")


try:
    cur = con.cursor()
    cur.execute("create table test(i int)")
except sqlite3.OperationalError:
    # Assume table already exists
    pass

cur.execute("insert into test(i) values (?)", (10,))
cur.execute("select i from test")
cur.fetchone()[0]

con.rollback()
cur.execute("select i from test")
cur.fetchone() is None

con.close()


# Test creating a connection with an empty string filename
con = sqlite3.connect("")
try:
    cur = con.cursor()
    cur.execute("create table test(i int)")
except sqlite3.OperationalError:
    # Assume table already exists
    pass

cur.execute("insert into test(i) values (?)", (10,))
cur.execute("select
