import ctypes
# Test ctypes.CFUNCTYPE
#
# This test needs to be run with the PYTHON_DEBUG_DONT_OPTIMIZE environment
# variable set to a non-empty string, otherwise all of the C-level code will
# be optimized out and it will appear as if nothing happened.

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

ftype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_char)

class X(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_char)]

# The CFUNCTYPE callbacks are only useful if they are
# used in a callbackprototyped function
lib.set_callback.argtypes = ctypes.c_int, ctypes.c_void_p
lib.set_callback.restype = None

lib.test_type.argtypes = ctypes.c_int, ctypes.POINTER(ctypes.c_
