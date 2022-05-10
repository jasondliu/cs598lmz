import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() with the default timeout value (5.0 seconds)
# and a short busy timeout (0.2 seconds).  There should be no timeout
# exceptions.  If the busy handler is invoked, the return value is
# True.  Otherwise the return value is False.

def busyhandler(count):
    if count > 3:
        return False
    return True

def test(dbname):
    con = sqlite3.connect(":memory:", timeout=5.0)
    con.execute("create table test(i)")
    con.execute("begin")
    con.execute("insert into test(i) values (1)")
    con2 = sqlite3.connect(":memory:", timeout=0.2)
    try:
        con2.execute("insert into test(i) values (2)")
    except sqlite3.OperationalError:
        con2.rollback()
    con.execute("commit")
    con.execute("insert into test(i) values (3)")
    con2.close()
    con.close()

