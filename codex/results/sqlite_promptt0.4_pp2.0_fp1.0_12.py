import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()
cursor.execute("create table test(id int)")
cursor.execute("insert into test(id) values (1)")
cursor.execute("select * from test")
print(cursor.fetchone())
conn.close()

# Test sqlite3.connect() with timeout
conn = sqlite3.connect(":memory:", timeout=5.0)
cursor = conn.cursor()
cursor.execute("create table test(id int)")
cursor.execute("insert into test(id) values (1)")
cursor.execute("select * from test")
print(cursor.fetchone())
conn.close()

# Test sqlite3.connect() with isolation_level
conn = sqlite3.connect(":memory:", isolation_level=None)
cursor = conn.cursor()
cursor.execute("create table test(id int)")
cursor.execute("insert into test(id) values (1)")
cursor.execute
