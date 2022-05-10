import ctypes
# Test ctypes.CFUNCTYPE

from ctypes import *
import _ctypes_test

# callback function
def py_callback(x):
    print("py_callback: x =", x)
    return x + 2

# define a callback function prototype
CALLBACKFUNC = CFUNCTYPE(c_int, c_int)

# convert the Python function into C callback function
c_callback = CALLBACKFUNC(py_callback)

# call a C function
