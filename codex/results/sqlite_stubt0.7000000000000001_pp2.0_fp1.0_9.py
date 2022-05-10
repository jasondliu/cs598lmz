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

def test_function():
    lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library('sqlite3'))
    lib.sqlite3_db_config.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int]
    lib.sqlite3_db_config.restype = ctypes.c_int
    lib.sqlite3_db_config(None, 99, 1)

    db = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    db.create_function("test", 1, my_cb)
    db.cursor().execute("select test(?);", (42,)).fetchone()[0]

test_function()

def target():
    for i in range(48):
        test_function()

ts = [ threading.Thread(target=target) for i in range(4) ]

for t in ts:
    t.start()

for t in ts
