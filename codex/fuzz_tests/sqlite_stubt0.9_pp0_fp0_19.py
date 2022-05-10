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


lib = ctypes.util.find_library("sqlite3")
if lib == None:
    print("libsqlite3 not found")
    exit(1)

print(lib)
sqlite3 = ctypes.cdll.LoadLibrary(lib)

sqlite3.sqlite3_config(2, 2)

rc = sqlite3.sqlite3_open(":memory:", ctypes.byref(my_threading_local.db))
if rc:
    print("sqlite3 could not be opened. error code = {}".format(rc))
    exit(1)

cb = ctypes.CFUNCTYPE(ctypes.c_int)(my_cb)
rc = sqlite3.sqlite3_test_control(1, my_threading_local.db, cb)
if rc:
    print("sqlite3_test_control could not be called. error code = {}".format(rc))
    exit(1)


sqlite3.sqlite3_close(my_threading_local.db)
