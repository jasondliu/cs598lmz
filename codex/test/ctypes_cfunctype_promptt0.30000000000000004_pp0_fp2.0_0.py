import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# a function pointer
Callable = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# a function taking a function pointer
