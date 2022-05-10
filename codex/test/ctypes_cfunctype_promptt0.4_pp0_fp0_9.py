import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
# restype and argtypes are passed to the constructor of the appropriate
# ctypes type.  The returned object is a callable object, which will
# call a C function based on the restype and argtypes.

# XXX We need a better way to test this.

Callable = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

