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

def my_cb_closed(p):
    return my_threading_local.a.close()


if __name__ == "__main__":
    try:
        sqlite3.sqlite3_enable_shared_cache(True)
    except:
        pass

    ctypes.CDLL(ctypes.util.find_library("sqlite3"), ctypes.RTLD_GLOBAL)

    sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_URI, True)
    sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_MULTITHREAD, True)

    sqlite3.sqlite3_enable_load_extension(True)

    my_connection = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    my_connection.execute("CREATE TABLE test (a, b)")
    my_connection.execute("INSERT INTO test VALUES (1, 2)")
    my_connection.execute("INSERT INTO test VALUES (5,
