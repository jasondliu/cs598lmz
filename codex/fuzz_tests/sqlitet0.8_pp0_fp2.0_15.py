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

print("init")
sqlite3.sqlite3_initialize()
print("init done")

libdb_file = ctypes.util.find_library("db")
if libdb_file is not None:
    libdb = ctypes.CDLL(libdb_file)

    libdb.db_create.argtypes = [ctypes.c_char_p, ctypes.c_uint32]
    libdb.db_create.restype = ctypes.c_void_p

    libdb.db_open.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p]
    libdb.db_open.restype = ctypes.c_int

    dbp = None
    if libdb.db_create(ctypes.c_char_p(b"test"), 0) == 0:
        print("db create failed")
        libdb.dbsys_abort()

    if libdb.db_open(dbp, ctypes.c_char_p(b"test
