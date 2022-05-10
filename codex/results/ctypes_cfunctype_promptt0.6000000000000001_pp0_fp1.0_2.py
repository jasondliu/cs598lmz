import ctypes
# Test ctypes.CFUNCTYPE.

# This test is specific to the callable object implementation of
# CFUNCTYPE.  It is not intended to test the Python-level CFUNCTYPE
# class.

import _ctypes_test

lib = _ctypes_test.dll

# prototype a function
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# define the function
def func(a, b):
    return a + b

# cast it to the prototype
f = prototype(func)

# call the function
res = f(2,3)

if res != 5:
    raise RuntimeError("function returned %d, expected 5" % res)
