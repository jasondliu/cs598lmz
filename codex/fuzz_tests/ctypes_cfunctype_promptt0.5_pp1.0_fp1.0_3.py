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
_ctypes_test.set_callback(c_callback)
_ctypes_test.call_callback(1)

# convert the Python function into C callback function
c_callback = CALLBACKFUNC(lambda x: x + 3)

# call a C function
_ctypes_test.set_callback(c_callback)
_ctypes_test.call_callback(1)
