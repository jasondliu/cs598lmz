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
    u = ctypes.CDLL(ctypes.util.find_library('user32'))
    u.MessageBoxW.argtypes = [ctypes.c_int, ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.c_int]
    u.MessageBoxW(0, "Hello", "Hello", 0)

    c = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    c.enable_shared_cache(1)
    c.create_collation("test", my_cb)

    conn = my_threading_local.a
    conn.execute("select test(3, 4)")

if __name__ == "__main__":
    main()
</code>

