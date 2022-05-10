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

    return 10

# Prints out the value and then returns it.
def my_trace_cb(p, *args):
    rc = p.trace(my_trace_cb, *args)
    print(p, ":", str(args))
    return rc

def sqlite3_open(filename, flags, vfs):
    p = ctypes.pythonapi.sqlite3_open_v2(filename, flags, vfs)
    rc = p.trace(my_trace_cb, p)
    if rc:
        raise RuntimeError("sqlite3_open() failed")
    return p

libc = ctypes.CDLL(ctypes.util.find_library("c"))
db = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

def main():
    # Create the function.
    db.create_function("my_cb", 0, my_cb)

    # Register our custom VFS.
    sqlite3.enable_callback_tracebacks(True)
    vfs = sqlite3.vfs.
