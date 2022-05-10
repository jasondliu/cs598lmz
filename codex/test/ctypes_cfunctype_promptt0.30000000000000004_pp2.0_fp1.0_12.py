import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# Test if a CFUNCTYPE(c_int) can be called with a Python int argument
# and returns a Python int.

Callable = ctypes.CFUNCTYPE(ctypes.c_int)

