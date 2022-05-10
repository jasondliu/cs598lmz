import ctypes
# Test ctypes.CFUNCTYPE

# This test is intended to be run with a debug build of Python.
# It will crash if the debug build is not used.

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This function is not called, but it must be declared,
# otherwise the test will crash.
lib.my_callback.restype = ctypes.c_int
lib.my_callback.argtypes = (ctypes.c_int, ctypes.c_int)

# This function is called, but it must not be declared,
# otherwise the test will crash.
#lib.my_callback2.restype = ctypes.c_int
#lib.my_callback2.argtypes = (ctypes.c_int, ctypes.c_int)

lib.set_callback.argtypes = (ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int),)

def my_callback(a, b):
    print("my_callback", a, b)
