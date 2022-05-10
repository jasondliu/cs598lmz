import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

restype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
