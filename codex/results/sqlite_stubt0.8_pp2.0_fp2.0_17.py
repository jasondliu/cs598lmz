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

def test_set_authorizer():
    # Check that a thread can call set_authorizer()

    dll = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    sqlite3_config = dll.sqlite3_config
    sqlite3_config.argtypes = [ctypes.c_int, ctypes.c_void_p]

    my_cb_func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)

    sqlite3_config(2, my_cb_func)
    
    with sqlite3.connect(DB_URI, uri=True, factory=deleting_conn) as a:
        a.execute("create table test (x)")

        my_thread = threading.Thread(target=lambda: test_fn())
        my_thread.start()
        my_thread.join()

        my_a = my_threading_local.a

        # Check that a can't do it either
        with pytest.
