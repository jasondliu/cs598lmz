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

    return 100

def test_extension_is_loaded():
    if not sqlite3.sqlite_version_info >= (3, 7, 16):
        pytest.skip("requires sqlite version 3.7.16 or greater")

    sqlite3.enable_callback_tracebacks(True)
    db = sqlite3.connect(DB_URI, uri=True)
    db.enable_load_extension(True)
    db.execute("SELECT load_extension(%s, %s)" % (ctypes.util.find_library("test"), "test"))
    assert db.execute("SELECT test(1, 2)").fetchall() == [(1,)]
    del db

def test_callback_is_thread_local():
    if not sqlite3.sqlite_version_info >= (3, 7, 16):
        pytest.skip("requires sqlite version 3.7.16 or greater")

    sqlite3.enable_callback_tracebacks(True)
    db = sqlite3.connect(DB_URI, uri=True)
    db.enable
