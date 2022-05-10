import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

try:
    dll = ctypes.CDLL(_ctypes_test.__file__)
except WindowsError:
    import os
    dll = ctypes.CDLL(os.path.splitext(_ctypes_test.__file__)[0] + ".dll")

# This is a function that takes a function pointer as argument
# and calls it.
CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

