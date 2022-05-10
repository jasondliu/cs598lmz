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

def my_cb_2():
    a = sqlite3.connect(DB_URI, factory=deleting_conn)
    a.create_function("test", 2, test_fn)
    my_threading_local.a = a
    return 1

def test_fn(a, b):
    return a

class TestError(Exception):
    pass

def load_pysqlite():
    lib = ctypes.util.find_library('pysqlite2')
    if not lib:
        raise TestError('pysqlite2 library not found.')
    pysqlite = ctypes.CDLL(lib)
    pysqlite.sqlite3_enable_shared_cache(1)

    return pysqlite

def make_thread(pysqlite, db_uri):
    def run():
        connection_factory = sqlite3.Connection
        def my_init(connection_factory, db_uri):
            my_threading_local.a = sqlite3.connect(factory=connection_factory)
