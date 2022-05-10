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

def test_callback():
    ctypes.CDLL(ctypes.util.find_library('sqlite3')).sqlite3_enable_shared_cache(1)

    conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    conn.enable_load_extension(True)
    conn.load_extension('sqlite3_testext')
    conn.create_function('my_cb', 0, my_cb)

    conn.execute('select my_cb()')

    del conn

sqlite3.register_converter("TEST", lambda x: x)

def test_register_converter():
    conn = sqlite3.connect(":memory:", uri=True)
    c = conn.cursor()
    c.execute("select 1 as test")
    assert c.fetchone()[0] == b"1"
    c.execute("select 1 as test")
    assert c.fetchone()[0] == b"1"
    c.close()
    conn
