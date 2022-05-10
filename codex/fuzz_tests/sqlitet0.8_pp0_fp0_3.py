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
    # setup
    try:
        conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
        conn.execute("create table t(a)")
        conn.execute("insert into t values (?)", [42])
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(e)
        return 1

    # ctypes setup
    lib = ctypes.util.find_library("sqlite3")
    if lib is None:
        raise Exception("can't find sqlite3 library")
    sqlite3_open = ctypes.CDLL(lib).sqlite3_open
    sqlite3_open.restype = ctypes.c_int
    sqlite3_open.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p)]

    # threading setup
    threads = []
    try:
        for i in range(0, 10):
            t = threading.Thread(target
