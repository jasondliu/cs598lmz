import ctypes
# Test ctypes.CFUNCTYPE on a simple function.

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

FuncPtr = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

