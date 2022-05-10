import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointer must have one integer argument, and returns
# an integer.

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is the function to call.

def callback(arg):
    print("callback called with argument", arg)
    return arg + 1

# This is the function that takes a function pointer as argument.

lib.pass_func(CALLBACK(callback))

# This is the function that takes a function pointer as argument.
# The function pointer must have one integer argument, and returns
# a pointer to a function.

CALLBACK = ctypes.CFUNCTYPE(CALLBACK, ctypes.c_int)

# This is the function to call.

def callback(arg):
    print("callback called with argument", arg)
    return CALLBACK(callback2)

def callback
