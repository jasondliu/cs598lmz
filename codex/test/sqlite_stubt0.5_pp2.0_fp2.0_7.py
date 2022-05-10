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

    def test_fn(a, b):
        return a

    a.create_function("test", 2, test_fn)

    return 1

if __name__ == "__main__":
    try:
        sqlite3.enable_callback_tracebacks(True)
    except AttributeError:
        # sqlite < 3.9
        pass

    sqlite3.enable_shared_cache(True)
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    sqlite3.register_adapter(int, lambda x: str(x))
    sqlite3.register_adapter(str, lambda x: x)
    sqlite3.register_converter("int", lambda x: int(x))
    sqlite3.register_converter("str", lambda x: x)
    lib.sqlite3_enable_shared_cache(1)
