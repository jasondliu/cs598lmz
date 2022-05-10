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

    return 1 # I did my work, SQLite can now continue loading.

def test_basic():
    lib = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
    lib.sqlite3_open(":memory:", ctypes.pointer(my_threading_local.db))
    assert lib.sqlite3_enable_load_extension(my_threading_local.db.p_db, 1) in (0, 1)
    lib.sqlite3_create_function(my_threading_local.db.p_db, b"mycb", 0, 1, my_cb, 0, 0)
    assert lib.sqlite3_load_extension(my_threading_local.db.p_db, b"mod_spatialite", b"sqlite3_modspatialite_init") == 0
    assert lib.sqlite3_db_config(my_threading_local.db.p_db, 99, 1, 0) == 99

def test_select_from_view():
    my_threading_local.
