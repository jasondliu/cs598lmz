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

sqlite3.api_init = my_cb


def main():
    a = sqlite3.connect(DB_URI, uri=True)
    print(my_threading_local.a)
    print(a)
    return 1

try:
    ctypes.cdll.LoadLibrary(ctypes.util.find_library("sqlite3"))
except:
    print("SKIP")
    raise SystemExit

sqlite3.sqlite_version_info
main()
