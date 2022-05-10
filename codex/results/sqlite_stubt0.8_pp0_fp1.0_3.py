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

# Register a finalizer to free the memory in the callback
def my_finalizer(p):
    del my_threading_local.a

lib = None

def setup_module():
    global lib
    os.environ['PYTHONTHREADSEXTRA'] = uri
    lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library('python{:d}.{:d}'.format(*sys.version_info[0:2])))
    lib.PyEval_InitThreads()

def test_sqlite3_join():
    pass
    # lib.PyEval_ReleaseThread(lib.PyGILState_GetThisThreadState())
    # lib.PyEval_ReleaseThread(lib.PyGILState_GetThisThreadState())
    # lib.PyEval_AcquireThread(lib.PyGILState_GetThisThreadState())
    # print('here')

def test_sqlite3_callback():
    lib.PyEval_ReleaseThread(lib.PyGILState_GetThisThreadState())
