import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')  in the cmd window, see if it work
# import sqlite3

# load shared library
# in ubuntu: sudo apt-get install libapr1
# in macport: cd /opt/local/lib, sudo port install apr1
apr1 = ctypes.cdll.LoadLibrary('/usr/lib/libapr-1.so.0') # macport
# apr1 = ctypes.cdll.LoadLibrary('/opt/local/lib/libapr-1.so.0') # macport
apr_pool_t=ctypes.c_void_p
apr_pool_create_ex_fn=ctypes.CFUNCTYPE(ctypes.c_int,ctypes.POINTER(apr_pool_t),ctypes.c_void_p,ctypes.c_void_p)
apr_pool_abort_set_fn=ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_void_p,ctypes.c_void_p,ctypes.c_void
