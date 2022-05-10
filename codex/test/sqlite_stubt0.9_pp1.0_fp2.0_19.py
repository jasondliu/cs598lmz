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

load_dll = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
load_dll.sqlite3_interrupt.argtypes = []
load_dll.sqlite33_busy_handler.argtypes = (ctypes.c_void_p, ctypes.c_void_p,
                                           ctypes.c_int)

class Thread(threading.Thread):
    def run(self):
        a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
        my_threading_local.a = a
        b = my_threading_local.a.execute("select 1;").next()

threads = []
for i in range(25):
    t = Thread()
    threads.append(t)
    t.start()

load_dll.sqlite3_busy_handler(None, my_cb, 1)
load_dll.sqlite3_interrupt()
