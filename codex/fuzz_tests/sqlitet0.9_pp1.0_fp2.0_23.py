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
    
    sqlite3.enable_callback_tracebacks(True)

    dllname = ctypes.util.find_library('c')
    cdll = ctypes.CDLL(dllname, ctypes.RTLD_GLOBAL)
    c_open = cdll.fopen
    c_open.retype = ctypes.c_void_p
    c_open.argtypes = [ctypes.c_char_p]

    # open some C file handle, so that it can grab the GIL from
    # sqlite3 internals without ever being closed
    c_open(b"/dev/null")

    t = threading.Thread(target=my_cb, args=(1,))
    t.start()
    t.join()

    import gc
    gc.collect()
    sleep(0.2) # help to see the memory leak

    # give connection example to sqlite3 internals, so that sqlite3
    # is mistakenly thinks that it is active
    try:
        sqlite3._trace_callback(None
