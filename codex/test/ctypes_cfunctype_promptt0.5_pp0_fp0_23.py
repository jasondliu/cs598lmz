import ctypes
# Test ctypes.CFUNCTYPE
from ctypes import CFUNCTYPE
import _ctypes_test

# Python function
def func(a, b):
    return a+b

# Python callback
CALLBACK = CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
def py_callback(a, b):
    return a+b

# C callback
