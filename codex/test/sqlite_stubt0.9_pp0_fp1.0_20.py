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

lib.sqlite3_thread_cleanup()
lib.sqlite3_create_function.restype = ctypes.c_int
lib.sqlite3_create_function(None, ctypes.c_char_p(b"test"), 1, ctypes.c_int(0), ctypes.py_object(42))
lib.sqlite3_thread_cleanup()

sqlite3.sqlite_version_info

sqlite3.register_adapter(set, tuple)

sqlite3.sqlite_version_info

sqlite3.register_converter("test", lambda x: x)

lib.sqlite3_thread_cleanup()
lib.sqlite3_set_authorizer(None, ctypes.py_object(my_cb))

a0 = sqlite3.connect(":memory:")
a0.enable_load_extension(True)
