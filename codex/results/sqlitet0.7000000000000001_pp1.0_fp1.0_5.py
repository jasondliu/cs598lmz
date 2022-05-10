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

def main():
    libsqlite3 = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    open_cb = sqlite3.sqlite3_open_v2
    open_cb.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p), ctypes.c_int, ctypes.c_char_p]
    open_cb.restype = ctypes.c_int
    flags = 0x00000002 # SQLITE_OPEN_URI
    db = ctypes.c_void_p()
    try:
        open_cb(DB_URI.encode("ASCII"), ctypes.byref(db), flags, None)
    except sqlite3.DatabaseError as e:
        print(e)
    libsqlite3.sqlite3_commit_hook(db, my_cb, None)

main()
