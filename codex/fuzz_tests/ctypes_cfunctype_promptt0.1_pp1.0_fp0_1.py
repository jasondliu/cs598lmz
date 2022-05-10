import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointer must have one integer argument, and returns
# an integer.

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is the function to call.

def func(arg):
    print("func() called with %d" % arg)
    return arg * 2

# This is the function that takes a function pointer as argument.

lib.pass_func(CALLBACK(func))

# This is the function that takes a function pointer as argument.
# The function pointer must have no arguments, and returns an integer.

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int)

# This is the function to call.

def func():
    print("func() called")
    return 42

# This is the function that takes a function pointer as argument.

lib.pass_
