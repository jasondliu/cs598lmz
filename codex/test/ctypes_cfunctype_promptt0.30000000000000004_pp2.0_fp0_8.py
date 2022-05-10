import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function pointer type.
fptr = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is a function pointer.
