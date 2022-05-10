import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
with sqlite3.connect(":memory:") as con:
    print(con)
    print(con.execute("select 1").fetchone()[0])

# Test sqlite3.Connection()
con = sqlite3.Connection(":memory:")
print(con)
print(con.execute("select 1").fetchone()[0])

libsqlite3 = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
print(libsqlite3)

libsqlite3.sqlite3_initialize()

con = libsqlite3.sqlite3_open(b":memory:", ctypes.c_void_p())
print(con)

con = libsqlite3.sqlite3_open(b":memory:", ctypes.byref(ctypes.c_void_p()))
print(con)

# With a global lock, the call to sqlite3_open() blocks until the thread
# holding the lock releases it.
lock = threading.Lock()
lock.acquire()

t =
