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
    my_threading_local.a.close()
    return 1

def main():
    ctypes.CDLL(ctypes.util.find_library("sqlite3"), use_errno=True).sqlite3_open_v2(DB_URI.encode("utf-8"), ctypes.byref(ctypes.c_void_p()), 0x00000002, None)
    sqlite3.enable_callback_tracebacks(True)
    sqlite3.set_authorizer(my_cb)
    conn = sqlite3.connect(DB_URI, uri=True)
    conn.execute("SELECT test(1, 2)")
    sqlite3.set_authorizer(my_cb2)
    conn.execute("SELECT test(1, 2)")

main()
</code>

