import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# Make sure this doesn't crash
ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lib.my_callback)
