import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointer must take an integer argument, and return
# an integer.

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is the function that will be passed to the C function.

def func(n):
    print('func', n)
    return n * 2

# Call the C function, passing func as argument

lib.pass_func(CMPFUNC(func))

# This is a function that takes a function pointer as argument.
# The function pointer must take an integer argument, and return
# a pointer to a function.

CMPFUNC2 = ctypes.CFUNCTYPE(CMPFUNC, ctypes.c_int)

# This is the function that will be passed to the C function.

def func2(n):
    print('func2', n)
    return
