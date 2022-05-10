import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connection object
conn = sqlite3.connect(":memory:")
conn.execute("create table test(id integer primary key, name text)")
conn.execute("insert into test(id, name) values (1, 'foo')")
conn.execute("insert into test(id, name) values (2, 'bar')")
conn.execute("insert into test(id, name) values (3, 'baz')")
cursor = conn.execute("select * from test")
for row in cursor:
    print(row)

# Test sqlite3.connection object
conn = sqlite3.connect(":memory:")
conn.execute("create table test(id integer primary key, name text)")
conn.execute("insert into test(id, name) values (1, 'foo')")
conn.execute("insert into test(id, name) values (2, 'bar')")
conn.execute("insert into test(id, name) values (3, 'baz')")
cursor = conn.execute("select * from test")
for row in cursor:
    print(row)

# Test
