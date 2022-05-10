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

def my_final_cb(p):
    my_threading_local.a.close()
    return 1


def test_thread():

    conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn, check_same_thread = False)

    sqlite3.complete_statement("select 1")

    conn.enable_load_extension(True)


    sqlite3.sqlite3_enable_shared_cache(1)

    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        cdll = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
        cdll.sqlite3_config(ctypes.c_int(0x19), my_cb, my_final_cb, ctypes.pointer(ctypes.c_int(0)))

    cdll.sqlite3_shutdown()
    cdll.sqlite3_config(ctypes.c_int(0x19), None, None, ctypes.pointer(ct
