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

sqlite3.connection_hook = my_cb

libc = ctypes.CDLL(ctypes.util.find_library("c"), use_errno=True)

def main():
    with sqlite3.connect(DB_URI, uri=True) as connection:
        cursor = connection.cursor()

        cursor.execute("select test(1, 2)")

    while threading.active_count() > 1:
        continue

    print("del a")
    del my_threading_local.a

    libc.free(0)
    print("free")
    time.sleep(10)

if __name__ == "__main__":
    main()
