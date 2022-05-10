import ctypes
import ctypes.util
import threading
import sqlite3

my_threading_local = threading.local()

class deleting_conn(sqlite3.Connection):
    def __del__(self):
        self.close()

DB_URI = "file:test?mode=memory"

def my_cb(p):
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    def test_fn(a, b):
        return a

    a.create_function("test", 2, test_fn)

    my_threading_local.a = a

    return 1

sqlite3.sqlite3_config(SQLITE_CONFIG_URI, 1)
sqlite3.sqlite3_config(SQLITE_CONFIG_LOG, my_cb)

conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

cur = conn.cursor()

cur.execute("select test(1, 2)")

print(cur.fetchone())

cur.close()
conn.close()

print(my_threading_local.a)

print(ctypes.util.find_library("sqlite3"))

print(ctypes.util.find_library("sqlite3.so"))

print(ctypes.util.find_library("sqlite3.dll"))

print(ctypes.util.find_library("sqlite3.dylib"))

print(ctypes.util.find_library("sqlite3.a"))

print(ctypes.util.find_library("sqlite3.la"))
