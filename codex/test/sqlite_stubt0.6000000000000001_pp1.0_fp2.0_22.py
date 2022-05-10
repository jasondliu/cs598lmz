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
    ctypes.CDLL(ctypes.util.find_library('sqlite3')).sqlite3_shutdown()
    ctypes.CDLL(ctypes.util.find_library('sqlite3')).sqlite3_config(1, 1)
    ctypes.CDLL(ctypes.util.find_library('sqlite3')).sqlite3_initialize()

    sqlite3.enable_callback_tracebacks(True)
    sqlite3.enable_shared_cache(True)

    conn = sqlite3.connect(DB_URI, uri=True)
    conn.set_authorizer(my_cb)
    cursor = conn.cursor()
    cursor.execute("select test(1, 2)")

    conn.set_authorizer(my_cb2)
    cursor.execute("select test(1, 2)")

if __name__ == "__main__":
    main()
