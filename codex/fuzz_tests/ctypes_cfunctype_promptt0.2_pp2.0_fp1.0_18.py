import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
#
# restype: the result type
# argtypes: a sequence specifying the argument types
# use_errno: if True, the function will check for errors after
#            the call, and if one occured, raise a OSError exception
#            with errno set to the error code.
# use_last_error: if True, the function will check for errors after
#                 the call, and if one occured, raise a WindowsError
#                 exception with winerror set to the error code.
#
# The use_errno and use_last_error arguments can not be used together.

# XXX We should test the use_errno and use_last_error arguments

# XXX We should test the prototype attribute

# XXX We should test the errcheck attribute

# XXX We should test the restype attribute

# XXX We
