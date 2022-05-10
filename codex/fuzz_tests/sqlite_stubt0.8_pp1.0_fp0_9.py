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

class ThreadWrapper(threading.Thread):
    def run(self):
        self.ret = my_cb(None)

my_cb_p = sqlite3.SQLITE_CALLBACK(my_cb)
lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
lib.sqlite3_test_control(4, my_cb_p, None)
for i in range(1):
    t = ThreadWrapper()
    t.start()
    t.join()
    assert t.ret == 1
    del t
lib.sqlite3_test_control(-4)
