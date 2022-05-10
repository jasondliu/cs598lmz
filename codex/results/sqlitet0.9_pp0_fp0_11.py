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

sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_MULTITHREAD)
sqlite3.sqlite3_vfs_register(sqlite3.sqlite3_vfs_find("unix_unregister"), True)

lib = ctypes.util.find_library("sqlite3")
if not lib:
    raise RuntimeError("Cannot find libsqlite3.")

lib = ctypes.CDLL(lib, use_errno=True)

lib.sqlite3_open_v2.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p),
                                ctypes.c_int, ctypes.c_char_p]

if not lib.sqlite3_open_v2(DB_URI.encode("utf-8"),
                           ctypes.byref(ctypes.c_void_p()),
                           1 | 2 | 1024, "unix_unregister".encode("utf-8")) == 0:
    raise RuntimeError("Something
