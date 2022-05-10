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

lib = sqlite3.sqlite_version_info[0] >= 3 and ctypes.CDLL(ctypes.util.find_library("sqlite3")) or ctypes.CDLL("sqlite3.dll")

lib.sqlite3_activate_see.argtypes = (ctypes.c_char_p,)
lib.sqlite3_activate_see.restype = ctypes.c_int

lib.sqlite3_db_config(ctypes.c_void_p(), 9, 1, None)

lib.sqlite3_activate_see(b"test")

conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

conn.set_progress_handler(my_cb, 100000)

cur = conn.cursor()

cur.execute("select * from sqlite_master")

print(cur.fetchall())

cur = my_threading_local.a.cursor()

cur.execute("select * from sqlite_master")

print(cur.fetch
