import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
# restype: the result type
# argtypes: a sequence specifying the argument types
# use_errno: if True, the function will set the global variable
#            ctypes.get_errno() in case a function call failed.
# use_last_error: if True, the function will set the Win32 last error
#                 value in case a function call failed.
#                 This is only meaningful on Windows.

# int func(int, int)
func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(("func", lib))
print func(1, 2)

# int func2(int, int)
func2 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_
