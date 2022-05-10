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

def my_cb2(p):
    a = my_threading_local.a

    a.execute("select test(1, 2)")

    return 1

libc = ctypes.CDLL(ctypes.util.find_library("c"))
libc.fork.restype = ctypes.c_int

libsqlite3 = ctypes.CDLL(ctypes.util.find_library("sqlite3"))

libsqlite3.sqlite3_config(6, 1)
libsqlite3.sqlite3_config(5, 1)

libsqlite3.sqlite3_config(1, my_cb, 0)
libsqlite3.sqlite3_config(2, my_cb2, 0)

db = sqlite3.connect(DB_URI, uri=True)

libsqlite3.sqlite3_enable_shared_cache(1)

cursor = db.cursor()

libc.fork()

cursor.execute("select 1")
</code>

