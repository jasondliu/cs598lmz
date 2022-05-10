import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
# restype: the result type
# argtypes: a sequence specifying the argument types
# use_errno: a bool indicating whether the function uses C errno
# use_last_error: a bool indicating whether the function uses C GetLastError

# ctypes.CFUNCTYPE(None)
# ctypes.CFUNCTYPE(None, ctypes.c_int)
# ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)
# ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int, ctypes.c_int)
# ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)
# c
