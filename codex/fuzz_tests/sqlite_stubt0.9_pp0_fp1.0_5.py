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

    return 100

def my_cb2(p):
    my_threading_local.a.close()

class ArithmeticException(Exception):
    def __init__(self):
        super(ArithmeticException, self).__init__("ArithmeticException")

class IOException(Exception):
    def __init__(self):
        super(IOException, self).__init__("IOException")

class NullPointerException(Exception):
    def __init__(self):
        super(NullPointerException, self).__init__("NullPointerException")

try:
    lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library("python3.3"))
except Exception as e:
    print("========================================================================================")
    print("\nError: (%s) - %s" % (type(e), e))
    print("\nYou must set the environment variable 'LD_LIBRARY_PATH' to point to your Python 3.3")
    print("runtime libraries. If your Debian version is >= 7, Python 3.3 runtime libraries are")
    print
