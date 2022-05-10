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

if __name__ == '__main__':
    fun = ctypes.CDLL(ctypes.util.find_library('sqlite3')).sqlite3_threadsafe
    print(fun(), "== SQLITE_THREADSAFE_SERIALIZED")

    lib = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
    lib.sqlite3_thread_cleanup()

    print(lib)
    print(lib.shmdt, type(lib.shmdt))

    assert lib.sqlite3_config(lib.SQLITE_CONFIG_URI, 1) == 0
    assert lib.sqlite3_config(lib.SQLITE_CONFIG_MULTITHREAD) == 0

    c = sqlite3.connect(DB_URI, uri=True)
    assert c.isolation_level == None
    c.close()

    c = sqlite3.connect(DB_URI, uri=True, isolation_level=None)
    assert c.isolation_level == None
    c.create_function("
