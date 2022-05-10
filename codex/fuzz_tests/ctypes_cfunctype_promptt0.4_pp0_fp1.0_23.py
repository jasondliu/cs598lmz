import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This function takes a function pointer as argument
# and calls it.

# The prototype of the called function is:
# int func(int)

CALLFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# The prototype of the calling function is:
# int call_func(int (*func)(int), int arg)

call_func = lib.call_func
call_func.argtypes = (CALLFUNC, ctypes.c_int)
call_func.restype = ctypes.c_int

# A simple function
def func(arg):
    print("func called with", arg)
    return arg * 2

# A function with a different prototype
def func_2(arg):
    print("func_2 called with", arg)
    return arg * 3

# This function takes a function pointer as argument
# and calls it.

# The prototype of the called function is
