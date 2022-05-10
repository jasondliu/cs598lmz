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

def my_thread():
    p = ctypes.POINTER(ctypes.c_int)()
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    lib.sqlite3_thread_cleanup()
    lib.sqlite3_threadsafe()
    lib.sqlite3_open_v2(DB_URI, ctypes.byref(p),
                        1 | 2 | 4 | 8 | 16, None)

    lib.sqlite3_set_authorizer(p.contents, my_cb, None)

    lib.sqlite3_exec(p.contents, "SELECT test(1, 2)", None, None, None)

    lib.sqlite3_close(p.contents)

t = threading.Thread(target=my_thread)
t.start()
t.join()

try:
    conn = my_threading_local.a
except AttributeError:
    assert False, "No thread local connection object."

conn.close()
