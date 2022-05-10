import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument
# and calls it.
CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is the function pointer type the CALLBACK function
# expects.
FUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is the function we pass to the CALLBACK function.
def func(n):
    print('func called with', n)
    return n * 2

# This is the function that calls the CALLBACK function.
def callback(n):
    print('callback called with', n)
    return lib.callback(CALLBACK(n))

# This is the function that calls the CALLBACK function.
def callback2(n):
    print('callback2 called with', n)
    return lib.callback2(CALLBACK(n))

# This is the function that calls the
