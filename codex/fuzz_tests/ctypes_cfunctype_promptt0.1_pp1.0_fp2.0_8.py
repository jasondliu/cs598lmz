import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointer must have the same signature as the
# CFUNCTYPE function we create.
CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is the function that is called by the C library.
def callback(i):
    print("callback", i)
    return i + 1

# This is the function that calls the C library.
def test(i):
    print("test", i)
    return lib.test_callback(i, CALLBACKFUNC(callback))

print(test(5))
