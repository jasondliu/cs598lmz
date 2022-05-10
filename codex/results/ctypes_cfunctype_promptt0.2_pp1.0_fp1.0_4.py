import ctypes
# Test ctypes.CFUNCTYPE

# This test is for the case where the function is called with
# a pointer to a structure.

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

# ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
#
# restype: the result type
# argtypes: a sequence of the argument types
# use_errno: if True, the function will check for -1, and raise an
# OSError if the result is -1.
# use_last_error: if True, the function will call GetLastError()
# and raise a WindowsError if the result is not zero.

# The function takes a pointer to a structure, and returns the sum
# of the two members.

f = lib.sum_integers_in_structure
f.argtypes
