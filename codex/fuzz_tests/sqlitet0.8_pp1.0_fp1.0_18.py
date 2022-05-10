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

def my_cb_2(p):
    a = my_threading_local.a

    try:
        a.execute("select test(?, ?)", (1,2)).fetchall()
    except sqlite3.OperationalError:
        print("Could not create thread callback")
    else:
        print("Created thread callback")

    return 1

def main():
    # Initialize sqlite3
    libsqlite3 = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    libsqlite3.sqlite3_config(ctypes.c_int(4), ctypes.c_int(1))  # SQLITE_CONFIG_MULTITHREAD=4; SQLITE_CONFIG_SERIALIZED==1
    libsqlite3.sqlite3_initialize()

    # Register first thread callback
    tcb = ctypes.CFUNCTYPE(ctypes.c_int)(my_cb)
    libsqlite3.sqlite3_thread_init(libsqlite3.sqlite3_initialize)
