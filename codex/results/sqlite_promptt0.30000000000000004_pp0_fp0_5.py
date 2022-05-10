import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("create table test (id integer primary key, name text)")
c.execute("insert into test (name) values (?)", ("foo",))
c.execute("insert into test (name) values (?)", ("bar",))
c.execute("select id, name from test")
print(c.fetchall())

# Test sqlite3.Row
conn = sqlite3.connect(":memory:")
conn.row_factory = sqlite3.Row
c = conn.cursor()
c.execute("select 'John' as name, 42 as age")
row = c.fetchone()
print("name:", row["name"])
print("age:", row["age"])

# Test sqlite3.Connection.create_function()
def double(x):
    return x * 2

conn = sqlite3.connect(":memory:")
conn.create_function("double", 1, double)
c = conn.cursor()
c.execute("
