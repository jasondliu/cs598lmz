import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
# restype: the result type
# argtypes: a sequence specifying the argument types
# use_errno: if True, the function will set the global variable errno
#            if an error occurs, and the caller should check errno
#            after the call.
# use_last_error: if True, the function will set the Win32 last error
#                 if an error occurs, and the caller should check
#                 the last error after the call.

# The function prototype is:
# int func(int, int)

