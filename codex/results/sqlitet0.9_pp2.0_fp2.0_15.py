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


libname = ctypes.util.find_library("sqlite3")
sqlite3 = ctypes.CDLL(libname)

sqlite3.sqlite3_shutdown();
sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_URI, 1);
sqlite3.sqlite3_initialize();

EMAKE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)
make = EMAKE(my_cb)

sqlite3.sqlite3_scalar_function_overload(
    -1,
    ctypes.cast(
        b'make',
        ctypes.POINTER(ctypes.c_char)),
    -1,
    make,
    None)

num_threads = 10

def worker():
    conn = sqlite3.connect(DB_URI)
    try:
        conn.execute('SELECT make(1)')
    finally:
        conn.close()

threads = [threading.Thread(target=worker
