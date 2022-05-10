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

def my_init_callback():
    return my_cb

@functools.lru_cache()
def get_sqlite_shared():
    return sqlite3.sqlite_version

def get_sqlite_dll():
    dll_path = ctypes.util.find_library("sqlite3")
    return ctypes.CDLL(dll_path)


def register_c_callback():
    dll = get_sqlite_dll()
    init_callback = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_init_callback)
    dll.sqlite3_initialize.argtypes = []
    dll.sqlite3_initialize()
    dll.sqlite3_auto_extension.argtypes = [init_callback]
    dll.sqlite3_auto_extension(init_callback)


def connect():
    #sqlite3.sqlite_version = "3.30.1"
    #get_sqlite_shared.cache_clear()

