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

clib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
clib.sqlite3_threadsafe()
clib.sqlite3_busy_handler.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)
clib.sqlite3_busy_handler.restype = None

def main():
    for i in range(100):
        print("Run {}".format(i))
        sqlite3.sqlite_version_info

        a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
        clib.sqlite3_busy_handler(a.connection.ptr, my_cb, None)

        my_threading_local.a = a

        try:
            a.execute("select test(a,b) from a")
        except Exception as e:
            print("Error %r" % (e,))

if __name__ == "__main__":
    main()
