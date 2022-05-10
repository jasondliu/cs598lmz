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
lib.sqlite3_db_config(0, 99, 1)

lib.sqlite3_enable_shared_cache(1)
lib.sqlite3_enable_load_extension(1)
lib.sqlite3_config(7, my_cb, 0)

a = sqlite3.connect(DB_URI, uri=True)

a.execute("SELECT load_extension('mod_spatialite')")
a.execute("SELECT load_extension('mod_spatialite')")
a.execute("SELECT load_extension('mod_spatialite')")
a.execute("SELECT load_extension('mod_spatialite')")
a.execute("SELECT load_extension('mod_spatialite')")
a.execute("SELECT load_extension('mod_spatialite')")
a.execute("SELECT load_extension('mod_spatialite')")
a.execute("SELECT load_extension('mod_spatialite')")
a
