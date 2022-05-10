import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointer must take an integer argument and return
# an integer.

CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is the function that we pass as argument to the
# function pointer.

def callback(arg):
    print "callback called with", arg
    return arg + 42

# This is the function that takes a function pointer as argument.

lib.pass_func(CALLBACKFUNC(callback))

# This is a function that takes a function pointer as argument.
# The function pointer must take an integer argument and return
# a pointer to a function.

CALLBACKFUNC2 = ctypes.CFUNCTYPE(CALLBACKFUNC, ctypes.c_int)

# This is the function that we pass as argument to the
# function pointer.

def callback2(arg):
