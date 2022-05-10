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

sqlite3.sqlite3_shutdown()

lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library("sqlite3"))

lib.sqlite3_config(ctypes.c_int(3), ctypes.py_object(my_cb))
lib.sqlite3_initialize()

threading.Thread(target=lambda x: (a := my_threading_local.a)(), args=(x,)).start()

for x in range(100):
    with sqlite3.connect(DB_URI, uri=True) as conn:
        conn.execute("select test(42, ?)", (x,))
