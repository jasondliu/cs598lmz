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
    a.close()
    return 1

libsqlite3_so_path = ctypes.util.find_library("sqlite3")
libsqlite3 = ctypes.CDLL(libsqlite3_so_path)

libsqlite3.sqlite3_enable_shared_cache(1)

libsqlite3.sqlite3_config(ctypes.c_int(0x00021000), my_cb, 0)
libsqlite3.sqlite3_config(ctypes.c_int(0x00021001), my_cb2, 0)

a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
b = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

print(a.execute("select test(1, 2)").fetchall())
</code>
The code is a bit ugly, but it is a minimal example.
The problem
