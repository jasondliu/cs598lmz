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

def my_cb2(p):
    a = my_threading_local.a
    a.execute("select test(?, ?)", (1, 2))
    return 1

def my_thread(lib):
    lib.sqlite3_open_v2(DB_URI.encode(), ctypes.byref(my_threading_local.db),
                        0x00000004 | 0x00000001, None)
    lib.sqlite3_create_function_v2(my_threading_local.db, b"test", 2, 4, None,
                                   my_cb2, None, None, None)
    lib.sqlite3_exec(my_threading_local.db, b"select test(1, 2)", None, None, None)

def main():
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    lib.sqlite3_open_v2.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p), ctypes.
