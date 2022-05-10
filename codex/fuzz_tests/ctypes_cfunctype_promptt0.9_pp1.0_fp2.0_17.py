import ctypes
# Test ctypes.CFUNCTYPE
from ctypes import *
from test.support import requires_type_collecting

library = ctypes.cdll.LoadLibrary(None)
try:
    c_ssize_t = ctypes.c_ssize_t
except AttributeError:
    c_ssize_t = ctypes.c_int64

def func(*args):
    return 42
CFUNCTYPE(ctypes.c_int)(func)
CFUNCTYPE(ctypes.c_int, ctypes.c_int)(func)
CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)
CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)
# func has no argtypes attribute, because it is not a ctypes callback function.
if hasattr(func, 'argtypes'):
    raise RuntimeError("func has argtypes??")
py_object = ctypes.py_object
CFUNCTYPE(
