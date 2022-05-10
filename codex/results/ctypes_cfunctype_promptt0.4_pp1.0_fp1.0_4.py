import ctypes
# Test ctypes.CFUNCTYPE
import _ctypes_test

def func(x):
    return x * 2

# func is a Python function.  It can be passed to ctypes
# functions expecting a C callback.

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# The C callback is converted to a Python object.
# It is called from C, and the integer value is returned.

c_func = CALLBACK(func)

# The Python callback is passed to a C function.
# The C function calls the Python callback and returns the result.

res = _ctypes_test.lib.test_callback(c_func, 1)
if res != 2:
    raise Exception("Bad result from callback")

# The Python callback is passed to a C function.
# The C function calls the Python callback, and raises
# an exception.  The exception is converted to a C
# exception, and the C function returns NULL.

try:
    _ctypes_test.lib.test_callback(c_func, -1)
except Value
