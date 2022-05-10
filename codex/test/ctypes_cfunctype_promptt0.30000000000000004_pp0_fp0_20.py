import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
#
# restype: the result type
# argtypes: a sequence specifying the argument types
# use_errno: if True, the function will set the Python variable
#            ctypes.get_errno() to the value returned by the C function.
# use_last_error: if True, the function will set the Python variable
#                 ctypes.get_last_error() to the value returned by the C
#                 function.

# XXX This is a hack to get the function prototype for the function
# XXX 'my_sqrt' in the _ctypes_test dll.  It would be better to
# XXX declare the function prototype in a header file, and include
# XXX that header file here.

class X(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double)]

