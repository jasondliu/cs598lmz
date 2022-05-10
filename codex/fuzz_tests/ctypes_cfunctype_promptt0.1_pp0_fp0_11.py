import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as an argument.
# The function pointed to must take an integer argument, and return
# an integer.

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

@CMPFUNC
def func(arg):
    print("func", arg)
    return arg

lib.pass_func(func)

# This is a function that takes a function pointer as an argument.
# The function pointed to must take an integer argument, and return
# a pointer to a function.  The pointed-to function must take an
# integer argument and return an integer.

CMPFUNC2 = ctypes.CFUNCTYPE(CMPFUNC, ctypes.c_int)

@CMPFUNC2
def func2(arg):
    print("func2", arg)
    return func

lib.pass_func(func2(42))


