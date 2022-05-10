import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
# restype: the result type
# argtypes: a sequence specifying the argument types
# use_errno: if True, the function will set Python's C errno variable, and
#   if the function returns -1, it will raise an OSError exception
# use_last_error: if True, the function will set Python's C last_error variable,
#   and if the function returns -1, it will raise a WindowsError exception

# The function prototype is:
# int func(int, int, int)

# The function is defined in _ctypes_test.c as:
# int func(int a, int b, int c) {
#   return a + b + c;
# }

# The function is called in _ctypes_test.c as:
# func(1, 2, 3);


