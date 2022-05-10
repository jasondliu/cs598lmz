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

if sqlite3.sqlite3_open_v2 == None:
    print("sqlite3_open_v2() isn't available to sqlite.")
    sys.exit(0)

if sqlite3.sqlite_version_info >= (3, 7, 17):
    print("sqlite3_open_v2() isn't available to sqlite.")
    sys.exit(0)


sqlite_dll = ctypes.util.find_library("sqlite3")
if sqlite_dll == None:
    print("sqlite3 library not found")
    sys.exit(0)

sqlite = ctypes.CDLL(sqlite_dll)

my_cb_addr = ctypes.cast(my_cb, ctypes.c_void_p).value
print("my_cb_addr = %d" % my_cb_addr)

sqlite3_open_v2 = sqlite3.sqlite3_open_v2
sqlite3_open_v2.argtypes = [ctypes.c_char_p, ctypes.PO
