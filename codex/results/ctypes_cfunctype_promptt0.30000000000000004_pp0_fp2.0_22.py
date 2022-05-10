import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call_function takes a function pointer as first argument,
# and an integer as second argument.  The function is called
# with the integer as argument, and the function returns the
# integer.

CALLFUNCTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def func(arg):
    return arg

# This is the function we pass to call_function
# It calls the function passed to it as first argument
# with the integer passed as second argument

def call_func(func, arg):
    return func(arg)

# The function pointer we pass to call_function

CALLFUNCTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# call_function is a simple function taking a function
# pointer and an integer as arguments.  It calls the
# function with the integer as argument, and returns
# the result.


