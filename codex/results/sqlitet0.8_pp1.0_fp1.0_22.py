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

def test_nested_thread():
    # Allocate a nested interpreter with a custom callback.
    nested_interpreter = ctypes.c_void_p()
    fn = my_cb
    fn_ptr = ctypes.cast(ctypes.byref(fn), ctypes.c_void_p)
    sqlite3.sqlite3_nested_interp_init(fn_ptr, ctypes.byref(nested_interpreter))

    # Run script in nested interpreter
    sqlite3.sqlite3_nested_interp_step(nested_interpreter, "SELECT test(17, 23)")

    # Check results (use global uri)
    conn = sqlite3.connect(":memory:")
    assert conn.execute("SELECT test(17, 23)").fetchone() == (17,)

    # Free the nested interpreter and all resources associated with it.
    sqlite3.sqlite3_nested_interp_free(nested_interpreter)

def my_cb_open(p):
    uri =
