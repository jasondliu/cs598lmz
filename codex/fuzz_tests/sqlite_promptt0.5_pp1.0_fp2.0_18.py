import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect and sqlite3.Cursor
import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("create table t (i int)")
c.execute("insert into t values (1)")
c.execute("select * from t")
assert c.fetchone() == (1,)
conn.close()
# Test sqlite3.Row
import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("create table t (i int, j int)")
c.execute("insert into t values (1, 2)")
c.execute("select * from t")
row = c.fetchone()
assert row[0] == 1
assert row[1] == 2
assert row["i"] == 1
assert row["j"] == 2
assert row.i == 1
assert row.j == 2
conn.close()
# Test sqlite3.Row.keys
import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.c
