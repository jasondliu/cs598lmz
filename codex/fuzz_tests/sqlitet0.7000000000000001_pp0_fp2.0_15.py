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

my_cb_p = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)

if __name__ == "__main__":
    sqlite3.register_adapter(deleting_conn, sqlite3.Connection)
    sqlite3.register_adapter(threading._local, lambda x: x)
    sqlite3.register_converter("_local", lambda x: my_threading_local)
    sqlite3.enable_callback_tracebacks(True)

    c_lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    c_lib.sqlite3_config(2, 1)

    c = sqlite3.connect(DB_URI, uri=True)

    c.execute("create table test(id integer primary key autoincrement)")

    c.create_function("my_cb", 1, my_cb_p)

    c.execute("select my_cb(?)", (None,))
    c.execute("
