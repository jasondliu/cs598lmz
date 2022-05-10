import ctypes
# Test ctypes.CFUNCTYPE(ctypes.c_int)

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# test None as argument type

try:
    ctypes.CFUNCTYPE(ctypes.c_int, None)
except TypeError:
    pass
else:
    raise Exception("Expected TypeError")


# test None as return type

try:
    ctypes.CFUNCTYPE(None, ctypes.c_int)
except TypeError:
    pass
