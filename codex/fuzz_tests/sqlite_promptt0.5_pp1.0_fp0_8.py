import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
import sqlite3
con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.execute("create table test(id integer primary key,value text)")
cur.executemany("insert into test(value) values (?)", [("a",), ("b",), ("c",)])
cur.execute("select id, value from test")
cur.fetchall()

# Test sqlite3.Connection
import sqlite3
con = sqlite3.connect(":memory:")
con.execute("create table test(id integer primary key,value text)")
con.executemany("insert into test(value) values (?)", [("a",), ("b",), ("c",)])
con.execute("select id, value from test")
con.fetchall()

# Test sqlite3.Cursor
import sqlite3
con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.execute("create table test(id integer primary key,value text)")
cur.executemany("insert into
