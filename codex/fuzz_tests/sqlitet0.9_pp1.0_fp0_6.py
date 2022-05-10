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

# ensure the DLL is found on Windows
ctypes.CDLL(ctypes.util.find_library("c"))

sqlite3.api_init(1, ctypes.c_void_p(threading.get_ident()))

sqlite3.api_init_thread(my_cb)

a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

race1 = threading.Event()

def write():
    my_threading_local.a.execute("create table test(a)")
    my_threading_local.a.commit()

    race1.set()

t = threading.Thread(target=write, args=())

t.start()

race1.wait()

a.execute("select test()")
