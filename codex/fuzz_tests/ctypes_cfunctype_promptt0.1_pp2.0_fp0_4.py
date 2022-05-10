import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointer must have the following signature:
# int func(double)

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_double)

# This is the function that will be passed to the C function.

def py_cmp_func(a):
    print("py_cmp_func called with", a)
    return -1

# Call the C function, passing the Python function as argument.

lib.set_cmp_func(CMPFUNC(py_cmp_func))

# Call the C function, which will call the Python function.

lib.call_cmp_func()
