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

def create_db():
    conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    conn.close()

def run_query():
    conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    conn.execute("select test(?)", ("hello",))
    threading.Timer(0.1, run_query).start()

if __name__ == "__main__":
    sqlite3.enable_callback_tracebacks(True)
    create_db()
    run_query()

    # find libsqlite3.so
    libsqlite_path = ctypes.util.find_library("sqlite3")

    if libsqlite_path is None:
        raise Exception("libsqlite3 not found")

    # load libsqlite3.so and attach callback
    libsqlite = ctypes.cdll.LoadLibrary(libsqlite_path)
    libsqlite.sqlite3_progress_handler.argtypes = [ctypes.c
