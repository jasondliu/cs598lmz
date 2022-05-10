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
    l = sqlite3.load_extension("libsqlitefunctions", ctypes.util.find_library("sqlitefunctions"))

    conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    conn.create_function("my_cb", 1, my_cb)

    cursor = conn.cursor()
    cursor.execute("select my_cb(1)")
    print(cursor.fetchone())
    print(my_threading_local.a)

    cursor.execute("select test(1, 2)")
    print(cursor.fetchone())

if __name__ == "__main__":
    main()
