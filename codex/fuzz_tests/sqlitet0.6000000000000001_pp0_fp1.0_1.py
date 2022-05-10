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

if __name__ == "__main__":
    sqlite3.threadsafety = 1
    sqlite3.enable_callback_tracebacks(True)

    ctypes.pythonapi.PyEval_InitThreads()

    my_threading_local.a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    my_threading_local.a.create_function("test", 2, lambda a, b: a)

    conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    conn.create_function("test", 2, lambda a, b: a)

    conn.threadsafety = 1
    conn.set_authorizer(my_cb)

    conn.execute("select test(1, 2)")
