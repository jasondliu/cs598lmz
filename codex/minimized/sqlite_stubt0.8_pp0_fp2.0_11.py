import ctypes.util
import sqlite3
class deleting_conn(sqlite3.Connection):
    def __del__(self):
        self.close()
def my_cb(p):
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
cb_ctype = ctypes.CFUNCTYPE(ctypes.c_int)
cb_p = cb_ctype(my_cb)
lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library('pthread'))
lib.pthread_create(None, None, cb_p, None)
