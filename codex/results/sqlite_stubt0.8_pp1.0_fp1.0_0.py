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

@pytest.fixture(scope="session")
def db(request):
    if sqlite3._sqlite3.threadsafety == "full":
        return sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    elif sqlite3._sqlite3.threadsafety == "serialized":
        sqlite3._sqlite3.sqlite3_config(sqlite3._sqlite3.SQLITE_CONFIG_SERIALIZED)
    else:
        sqlite3._sqlite3.sqlite3_config(sqlite3._sqlite3.SQLITE_CONFIG_MULTITHREAD)

    # Create a thread local callback
    global my_cb

    my_cb = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)

    sqlite3._sqlite3.sqlite3_thread_cleanup()
    sqlite3._sqlite3.sqlite3_thread_set_callback(my_cb)

    def fin():
        my
