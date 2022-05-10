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
c_callback = _ctypes_test.CALLBACK(py_callback)

# Test Python callback
assert _ctypes_test.test_callback(py_callback, 2, 3) == 5

# Test C callback
assert _ctypes_test.test_callback(c_callback, 2, 3) == 5

# Test Python function
assert _ctypes_test.test_callback(func, 2, 3) == 5

# Test Python function with CFUNCTYPE
cfunc = CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)
assert _ctypes_test.test_callback(cfunc,
