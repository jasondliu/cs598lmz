import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() works
con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.execute("create table test (id int primary key, data text)")
cur.execute("insert into test values(1, 'foo')")
cur.execute("insert into test values(2, 'bar')")
cur.execute("select * from test")
con.commit()
print cur.fetchall()
print "Done"
