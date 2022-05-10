import ctypes
import ctypes.util
import threading
import sqlite3
import traceback

import sys
import os

path = os.path.dirname(os.path.realpath(__file__))

clib = ctypes.util.find_library("c")
c = ctypes.CDLL(str(clib))

c.init_handle_exceptions()
c.handle_set_throw(1 if "--throw" in sys.argv else 0)
c.handle_set_print(1 if "--print" in sys.argv else 0)
c.enable_handle_exceptions()

sqlite3.enable_callback_tracebacks(True)

def delayed_assert(delay, condition):
    def f():
        if not condition():
            # Cause a segfault in the main thread
            c.void_throw_exception()
    print("Sleeping {} seconds before assert(0)".format(delay))
    assert(0 == python.sys.thread.sleep(delay * 1000))
    t = threading.Timer(1.09, f)
