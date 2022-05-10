import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointer must have the same signature as the
# CFUNCTYPE function we create.

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def py_cmp_func(a, b):
    print("py_cmp_func", a, b)
    return a - b

cmp_func = CMPFUNC(py_cmp_func)

lib.set_cmp_func(cmp_func)

# call the function pointer

lib.call_cmp_func(3, 4)

# call the function pointer from C

print(lib.test_cmp_func(3, 4))

# call the function pointer from C, with wrong argument type

try:
    lib.test_cmp_func(3, "hello")
except TypeError:
    print("Type
