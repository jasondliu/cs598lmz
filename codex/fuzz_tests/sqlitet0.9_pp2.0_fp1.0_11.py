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

sqlite3.sqlite3_test_control(sqlite3.SQLITE_TESTCTRL_PRNG_SEED, 123456) # to get reproducible results
sqlite3.sqlite3_test_control(sqlite3.SQLITE_TESTCTRL_LOAD_EXTENSION, sqlite3.reset_load_extension())
sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_URI, 1)

if ctypes.util.find_library('cfitsio.so'): # for e.g. Travis CI builds, where it's missing
    cfitsio = ctypes.CDLL('cfitsio.so')
    cfitsio.fits_open_file.res_type = ctypes.POINTER(ctypes.c_void_p)
    cfitsio.fits_get_hdu_num.argtypes = [ctypes.c_void_p, ctypes.c_int]
    cfitsio.fits_get_hdu_num.res_type = ctypes.c_int
    cfitsio
