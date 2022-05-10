import ctypes
# Test ctypes.CFUNCTYPE() with a function that returns a pointer.

import ctypes
import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that returns a pointer to the string "Hello World".
restype = ctypes.POINTER(ctypes.c_char)
