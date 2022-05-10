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

    return 1;

ctypes.pythonapi.PyEval_InitThreads()
tf = ctypes.pythonapi.Py_NewInterpreter()
# No idea why I got segfault if I did not call PyThreadState_Clear().
ctypes.pythonapi.PyThreadState_Clear(ctypes.py_object(tf))
ctypes.pythonapi.PyEval_ReleaseLock()

sqlite3.enable_callback_tracebacks(True)
sqlite3.SQLITE_OK
sqlite3.load_extension("./test.so", "sqlite3_extension_init")

a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
a.create_function("python_cb", 1, my_cb)

a.cursor().execute("select python_cb('spam')")
while True:
    pass
