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

def my_cb_wrap(n, pstr):
    return 1

class _TestExtension(AbstractSQLiteExtension):

    def __init__(self):
        super(_TestExtension, self).__init__(ctypes.CDLL(
            ctypes.util.find_library("memchr")))
        self.sqlite_extension_init = self._verify_decl("sqlite3_extension_init")
        self.sqlite_extension_init.argtypes = (py_object, py_object, py_object)\
            + (ctypes.POINTER(ctypes.c_int) * 4)
        self.sqlite_extension_init.restype = ctypes.c_int
        self.init_retval = self._extension_init()

    def _verify_decl(self, function_name, argtypes=(), restype=None):
        function_ptr = getattr(self.lib, function_name)
        function_ptr.argtypes = argtypes
        function_ptr.restype = restype
       
