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
    # load sqlite3_ext
    lib = ctypes.util.find_library("sqlite3_ext")
    if not lib:
        print("sqlite3_ext not found")
        sys.exit(1)
    sqlite3_ext = ctypes.CDLL(lib)

    # register function
    sqlite3_ext.sqlite3_ext_init(ctypes.c_int(0), None)
    sqlite3_ext.sqlite3_ext_register(b"my_cb", my_cb)

    # connect and test
    conn = sqlite3.connect(DB_URI, uri=True)
    cursor = conn.cursor()
    cursor.execute('''SELECT test(42, 23)''')
    print(cursor.fetchone())
    conn.close()

    # check if the global connection is closed
    cursor = my_threading_local.a.cursor()
    cursor.execute('''SELECT 1''')
    print(cursor.fetchone())
    my_thread
