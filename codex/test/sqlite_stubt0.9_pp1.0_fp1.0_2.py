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

sqlite3.sqlite3_enable_shared_cache(1)
lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
connection_hook = lib.sqlite3_connection_hook_with_config
connection_hook.restype = ctypes.c_int
connection_hook.argtypes = [ctypes.c_void_p, ctypes.CFUNCTYPE(ctypes.c_int, ctypes.py_object)]
connection_hook(None, connection_hook.argtypes[1](my_cb))

class Thread(threading.Thread):
    def run(self):
        db = sqlite3.connect(DB_URI, uri=True)
        cur = db.cursor()
        cur.execute("select test(1, 2)")
        db.commit()

def main():
    threading.current_thread().ident
    threads = [Thread() for i in range(5)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
   
