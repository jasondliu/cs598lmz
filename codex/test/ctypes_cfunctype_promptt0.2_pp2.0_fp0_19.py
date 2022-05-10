import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointer must have one integer argument, and returns
# an integer.

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is the function that is called by the C code.

def callback(arg):
    print("callback called with arg:", arg)
    return arg + 42

# This is the function that calls the C code.

def call_callback(callback):
    lib.call_callback(CALLBACK(callback), 5)

