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

def my_init(db_uri):
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    cb = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)
    lib.sqlite3_open_v2(db_uri.encode("utf-8"), ctypes.byref(ctypes.c_void_p()), 0x0003, None)
    lib.sqlite3_busy_handler(ctypes.c_void_p(), cb, None)

my_init(DB_URI)

def my_test():
    with sqlite3.connect(DB_URI, uri=True, factory=deleting_conn) as conn:
        conn.execute("select test(?, ?)", (1, 2))

threads = []
for i in range(10):
    t = threading.Thread(target=my_test)
    t.start()
    threads.append(t)

for t in threads:
