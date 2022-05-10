import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument
# and calls it.

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(arg):
    print("callback called with", arg)
    return arg + 1

# CallbackTest takes a function pointer as argument, calls it, and
# returns the result.

CallbackTest = lib.CallbackTest
CallbackTest.argtypes = CALLBACK,
CallbackTest.restype = ctypes.c_int

res = CallbackTest(CALLBACK(callback))
print("CallbackTest returned", res)

# This is a function that takes a function pointer as argument
# and calls it.

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def callback(arg1, arg2):
    print("callback called with", arg1,
