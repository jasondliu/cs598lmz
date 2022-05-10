import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
conn = sqlite3.connect(":memory:")
cur = conn.cursor()
cur.execute("create table data(x integer)")
cur.execute("insert into data values (1)")
# We can read it back in Python
cur.execute("select x from data")
print cur.fetchall()
# And it is stored in the database
cur2 = conn.cursor()
cur2.execute("select x from data")
print cur2.fetchall()
# Python objects can be stored as blob data
cur.execute("delete from data")
obj = ["this", "is", 4, 13327]
cur.execute("insert into data(x) values (?)", (sqlite3.Binary(pickle.dumps(obj, -1)),))
cur.execute("select x from data")
data = cur.fetchone()[0]
obj2 = pickle.loads(data)
print obj2, obj2 == obj
# pysqlite can also use sqlite3 extensions
# by default, but you have to supply the path to the extension library
# yourself

