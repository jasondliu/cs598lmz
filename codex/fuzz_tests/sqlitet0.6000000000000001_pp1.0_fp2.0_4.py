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

def test_create_function():
    ctypes.pythonapi.Py_InitModule4(
        "test_create_function",
        test_create_function.__dict__,
        "",
        None,
        ctypes.PY_VERSION_HEX)

    if sys.platform == "win32":
        sqlite3.sqlite3_enable_shared_cache(0)

    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    a.create_collation("my_collation", lambda x,y: -cmp(x,y))

    def test_fn(a, b):
        return a

    a.create_function("test", 2, test_fn)

    b = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    assert b.execute("select test(1, 2)").fetchone()[0] == 1

    b.enable_load_extension(True)
    b.load_extension("test_create_
