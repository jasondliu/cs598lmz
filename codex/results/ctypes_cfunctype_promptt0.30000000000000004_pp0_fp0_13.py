import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
#
# restype: the result type
# argtypes: a sequence specifying the argument types
# use_errno: if True, the function will check for errors after calling the
#   function, and will raise a OSError exception if one was set.
# use_last_error: if True, the function will check for errors after calling the
#   function, and will raise a WindowsError exception if one was set.
#   use_errno takes precedence over use_last_error.

f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(
        ("my_sqr", lib), ((1, "x"), (1, "y")))
assert f(5, 5) == 25

f = ctypes.CFUNCTYPE(ctypes
