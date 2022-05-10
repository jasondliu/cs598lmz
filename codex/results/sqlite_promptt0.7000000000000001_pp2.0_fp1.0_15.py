import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() as a context manager

libsqlite = ctypes.CDLL(ctypes.util.find_library('sqlite3'))

def busy_handler(dummy, count):
    if count == 0:
        print "busy handler called for first time"
    elif count == 1:
        print "busy handler called for second time"
    elif count == 2:
        print "busy handler called for third time"
    return 0

libsqlite.sqlite3_threadsafe()

# SQLITE_OPEN_FULLMUTEX mode will serialize access to the database
# connection, so we need to test that the context manager works even
# when the connection is already locked.
con = sqlite3.connect(":memory:", check_same_thread=False)
con.execute("create table test(x)")
con.execute("insert into test values (1)")
con.execute("insert into test values (2)")
con.execute("insert into test values (3)")
con.commit()

libsqlite.sqlite3_busy_
