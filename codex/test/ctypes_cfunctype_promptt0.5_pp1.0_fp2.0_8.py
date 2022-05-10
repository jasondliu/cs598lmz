import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

restype = ctypes.c_int
argtypes = (ctypes.c_int, ctypes.c_int)

# call_func is a CFUNCTYPE instance, call_func(42, 43) should return 42+43
