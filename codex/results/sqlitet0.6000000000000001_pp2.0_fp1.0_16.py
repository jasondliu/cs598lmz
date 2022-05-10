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

def test_conn_factory():
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    lib.sqlite3_open_v2(DB_URI.encode(), ctypes.byref(my_threading_local.conn), 1, None)
    lib.sqlite3_create_function_v2(my_threading_local.conn, "test_cb".encode(), 1, 1, None, ctypes.cast(my_cb, ctypes.c_void_p), None, None, None)
    my_threading_local.conn.execute("select test_cb(?)", (1,))

def test_conn_factory_threads():
    threads = [threading.Thread(target=test_conn_factory) for _ in range(2)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

try:
    test_conn_factory()
except sqlite3.ProgrammingError:
    # The test should fail with a
