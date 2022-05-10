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
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    lib.sqlite3_config(ctypes.c_int(4), ctypes.c_int(1))

    lib.sqlite3_enable_load_extension(None, 1)

    cb = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)

    lib.sqlite3_auto_extension(cb)

    conn = sqlite3.connect(DB_URI, uri=True)
    conn.enable_load_extension(True)
    conn.load_extension("./test_extension")

    cursor = conn.cursor()
    cursor.execute("select test(1, 2)")

    print(cursor.fetchall())

    cursor.execute("select test(1, 2)")

    print(cursor.fetchall())

    cursor.execute("select test(1, 2)")

