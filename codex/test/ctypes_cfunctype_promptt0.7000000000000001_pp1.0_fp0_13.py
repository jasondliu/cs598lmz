import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# Calling conventions.
cdecl = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
stdcall = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# argtypes and restype set.
