import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:") is corresponding to if sqlite3 was compiled 
# with SQLITE_THREADSAFE=0 or SQLITE_THREADSAFE=1.
def test_sqlite3_connect_memory():
    try:
        db = sqlite3.connect(":memory:")
        for i in range(4):
            db.execute("CREATE TABLE %s (id INT)" % i)
        db.execute("insert into 0 values (1)")
        db.execute("insert into 1 values (1)")
        db.execute("insert into 2 values (1)")
        db.execute("insert into 3 values (1)")
        db.execute("select * from 0")
        db.execute("select * from 1")
        db.execute("select * from 2")
        db.execute("select * from 3")
    except sqlite3.OperationalError as e:
        assert False, e

test_sqlite3_connect_memory()
#################################################################


import sqlite3
import threading

