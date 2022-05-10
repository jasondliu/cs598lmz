import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument
# and calls it.
CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is the function that will be called by the callback function
def py_callback(arg):
    print("callback called with argument", arg)
    return arg + 1

# This is the function that will be called by the callback function
def py_callback2(arg):
    print("callback2 called with argument", arg)
    return arg + 1

# This is the function that will be called by the callback function
def py_callback3(arg):
    print("callback3 called with argument", arg)
    return arg + 1

# This is the function that will be called by the callback function
def py_callback4(arg):
    print("callback4 called with argument", arg)
    return arg + 1

# This is the function that will be called by the callback
