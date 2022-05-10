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
    a.close()

    return 1

p = ctypes.POINTER(ctypes.c_int)()

if ctypes.c_int.in_dll(ctypes.util.find_library("sqlite3"), "sqlite3_threadsafe"):
    ctypes.cdll.LoadLibrary(ctypes.util.find_library('pthread')).pthread_create(ctypes.c_void_p(), ctypes.c_void_p(), ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb2), ctypes.c_void_p())
    lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library("sqlite3"))
    lib.sqlite3_db_config(lib.sqlite3_open(DB_URI.encode("UTF-8"), ctypes.byref(p)), 2, 1)
    lib.sqlite3_collation_needed16(
