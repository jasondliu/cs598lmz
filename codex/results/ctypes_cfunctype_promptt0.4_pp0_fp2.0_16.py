import ctypes
# Test ctypes.CFUNCTYPE

from ctypes import *

# CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
# -> function prototype
#
# restype: the result type
# argtypes: a sequence specifying the argument types
# use_errno: if True, the function will check for errors after
#   the call, and raise an exception if one occured.
# use_last_error: if True, the function will check for errors after
#   the call, and raise an exception if one occured.
#
# The function prototype can be called with any kind of argument
# compatible with the specified types.  The prototype checks the
# types at call-time, and raises a TypeError if they are incompatible.
#
# The call returns the result of the function call, converted to
# the specified result type.  If the result type is a primitive type
# and the call failed, a WindowsError exception is raised.
#
# The prototype can also be used as a decorator:
#
# @CFUNCTYPE(restype, argtypes...)
#
