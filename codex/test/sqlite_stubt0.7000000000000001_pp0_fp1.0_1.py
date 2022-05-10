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
    lib_fname = ctypes.util.find_library("sqlite3")
    lib = ctypes.CDLL(lib_fname)

    lib.sqlite3_initialize()

    lib.sqlite3_config(ctypes.c_int(lib.SQLITE_CONFIG_URI), my_cb, None)

    my_threading_local.a = sqlite3.connect(DB_URI, uri=True)

    try:
        my_threading_local.a.execute("SELECT test(1, 2, 3)")
    except sqlite3.OperationalError as e:
        assert e.args[0] == "too many arguments to function test"
    else:
        raise Exception("FAIL")

if __name__ == "__main__":
    main()
