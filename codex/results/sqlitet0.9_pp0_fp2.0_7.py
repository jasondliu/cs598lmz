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

def main(test_lib_uri):
    c = sqlite3.connect(test_lib_uri, uri=True, factory=deleting_conn)

    c.execute("ATTACH DATABASE '{}' AS 'test'".format(DB_URI))

    c.create_function("cpy", 0, my_cb)

    c.execute("SELECT cpy()")

    d = c.cursor()

    my_threading_local.a.close()

    del d
    del my_threading_local.a
    del c

    if ctypes.string_at(test_lib_uri) != b"":
        os.unlink(ctypes.string_at(test_lib_uri).decode())

if __name__ == "__main__":
    main(sys.argv[1])
