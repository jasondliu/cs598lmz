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

def main():
    c_cb = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)

    sqlite3.enable_callback_tracebacks(True)
    sqlite3.sqlite3_trace_v2(0, c_cb, None)

    conn = sqlite3.connect(DB_URI, uri=True)
    conn.execute("select test(1, 2)")

    del my_threading_local.a

if __name__ == "__main__":
    main()
</code>

