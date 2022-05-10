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
lib.sqlite3_open(DB_URI.encode('utf-8'), ctypes.pointer(p));
lib.sqlite3_profile(p, ctypes.CFUNCTYPE(None, ctypes.POINTER(sqlite3.sqlite3),
                                        ctypes.c_char_p,
                                        ctypes.c_int,
                                        ctypes.c_voidp)(my_cb),
                    None)

lib.sqlite3_open_v2(DB_URI.encode('utf-8'), ctypes.pointer(p),
                    sqlite3.SQLITE_OPEN_READWRITE |
                    sqlite3.SQLITE_OPEN_CREATE |
                    sqlite3.SQLITE_OPEN_URI,
                    NULL);
