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

def _main():
    libc = ctypes.CDLL(ctypes.util.find_library("c"))
    cb = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.py_object)(my_cb)
    libc.pthread_atfork(None, None, cb)
    print "main thread:", threading.current_thread().ident
    conn = sqlite3.connect(DB_URI, uri=True)
    conn.close()
    conn = None
    pid = os.fork()
    if pid == 0:
        conn = sqlite3.connect(DB_URI, uri=True)
        conn.execute("SELECT test(1, 2)")
        conn.close()
        os._exit(0)
    else:
        os.waitpid(pid, 0)

print "main thread:", threading.current_thread().ident
print "main thread:", threading.current_thread().__dict__

try:
    _main()
except IOError:
    traceback.print_
