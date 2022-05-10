import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a simple function that takes a pointer to a function
# as an argument, and calls the function.

# The function takes an integer argument, and returns an integer.

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(arg):
    print "callback called with", arg
    return arg

CALLBACKFUNC = ctypes.CFUNCTYPE(None, ctypes.c_int)

def callbackfunc(arg):
    print "callbackfunc called with", arg

# The prototype of the function is:
# int call_function(int (*func)(int), int arg)

call_function = lib.call_function
call_function.argtypes = (CALLBACK, ctypes.c_int)
call_function.restype = ctypes.c_int

# The prototype of the function is:
# void call_function2(void (*func)(int
