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

def test_cb():
    sqlite3.enable_callback_tracebacks(True)

    # Make sure the library is loaded:
    sqlite3.connect(DB_URI)

    sqlite3.register_adapter(type(ctypes.NULL), lambda x: None)
    sqlite3.register_adapter(ctypes.c_bool, lambda x: bool(x.value))
    ctype_func_type = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)
    libname = ctypes.util.find_library("sqlite3")
    if not libname:
        raise Exception("Failed to load sqlite3 library")
    sqlite3.load_batteries_in_dll(libname)
    sqlite3.enable_callback_tracebacks(True)
    c_cb = ctype_func_type(my_cb.im_func)
    cfunc = ctypes.CDLL(libname)
    ret = cfunc.sqlite3_progress_handler(255, 1,
