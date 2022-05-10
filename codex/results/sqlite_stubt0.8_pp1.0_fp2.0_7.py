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

def test_fn(a, b):
    return a

lib = None
for lib_name in ("sqlite3", "sqlite"): # for osx
    try:
        lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library(lib_name))
    except:
        pass
    if lib is not None:
        break
if lib is None:
    raise RuntimeError("Can't load sqlite")

def my_hook(p):
    print "Calling my hook"
    return 0

lib.sqlite3_open_v2(DB_URI, ctypes.byref(my_threading_local.db),
                    sqlite3.OPEN_READWRITE | sqlite3.OPEN_CREATE | sqlite3.OPEN_URI, None)
lib.sqlite3_create_function(my_threading_local.db, "test", 2, 1, my_threading_local.a, test_fn, 0, 0)
lib.sqlite3.sqlite3_set_authorizer(my_
