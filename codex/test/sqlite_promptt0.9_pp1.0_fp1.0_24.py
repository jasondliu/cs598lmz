import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:").isolation_level

# Test that threading without a mutex is still thread-safe
sqlite3.threadsafety = 0
# Test that a calling multiple times to threadsafety property is okay
sqlite3.threadsafety

# Test non BLOB I/O
conn = sqlite3.connect(":memory:")
cur = conn.cursor()
cur.execute("create table abc (a text, b text, c int)")
cur.execute("insert into abc values (1,'1',1)")
cur.execute("insert into abc values (2,'2',2)")
cur.execute("insert into abc values (3,'3',3)")
cur.execute("select * from abc")
cur.execute("select b, c from abc where a = 1")
cur.execute("delete from abc where a = 1")
cur.execute("select * from abc")

# Test BLOB I/O
cur.execute("create table abc (a blob, b blob, c blob)")
