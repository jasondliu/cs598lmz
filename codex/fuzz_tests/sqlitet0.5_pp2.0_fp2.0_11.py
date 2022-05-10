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
    my_threading_local.a.close()
    return 1

def main():
    sqlite3.enable_callback_tracebacks(True)

    sqlite3.sqlite3_shutdown()
    sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_URI, 1)
    sqlite3.sqlite3_initialize()

    sqlite3.sqlite3_enable_load_extension(True)

    lib = ctypes.util.find_library("sqlite3")

    f = ctypes.CDLL(lib)
    f.sqlite3_create_function_v2.argtypes = [
        ctypes.c_void_p,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_int,
        ctypes.c_void_p,
        ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p),
        ctypes.CFUNCTYPE(
