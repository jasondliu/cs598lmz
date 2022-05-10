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

class MyThread(threading.Thread):
    def run(self):
        p = ctypes.CFUNCTYPE( ctypes.c_int, ctypes.c_void_p )(my_cb)
        d = sqlite3.load_dll()
        sqlite3.api_user_data(p)
        d.sqlite3_config(sqlite3.SQLITE_CONFIG_URI, 1)

        a = sqlite3.connect(":memory:", uri=False)
        b = sqlite3.connect(DB_URI, uri=True)

        b.close()
        a.close()

m = {}
for x in range(10):
    t = MyThread()
    t.start()
    m[t] = 1

for t in m:
    t.join()
