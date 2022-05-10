import ctypes
# Test ctypes.CFUNCTYPE.
# http://bugs.python.org/issue16656

# NOTE: ctypes.CFUNCTYPE is not supported on all platforms,
# especially on Windows.  We therefore skip this test on Windows.

import sys
if sys.platform.startswith('win'):
    raise unittest.SkipTest("skipping ctypes.CFUNCTYPE test on Windows")

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a simple version of the CFUNCTYPE test in test_ctypes.
# It does not test the complete functionality of CFUNCTYPE, but
# it does test the bugfix for issue #16656.

class X(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int)]

lib.set_value.argtypes = [ctypes.c_int, ctypes.POINTER(X)]
lib.set_value.restype = None

def func(a, b):
    pass

CFUNC = c
