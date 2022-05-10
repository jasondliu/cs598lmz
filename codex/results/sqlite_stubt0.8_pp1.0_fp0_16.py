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

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
open = lib.sqlite3_open_v2
open.argtypes = (ctypes.c_char_p, ctypes.POINTER(ctypes.c_voidp), ctypes.c_int,
                 ctypes.c_char_p)

a = open(DB_URI.encode("utf-8"), None, 0, my_cb)

def A():
    b = my_threading_local.a
    print(b.execute("SELECT test(1, 2)"))

t = threading.Thread(target=A)
t.start()

while 1:
    pass
