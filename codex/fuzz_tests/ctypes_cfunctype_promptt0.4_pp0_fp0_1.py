import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

class Z(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

# XXX This test fails on 64-bit Linux, and I don't know why.
# It seems that the callback function is called, but the
# parameters are not passed correctly.  The test passes on
# Windows and 64-bit OSX.
if ctypes.sizeof(ctypes.c_void_p) == 4:
    # XXX This test fails on 64-bit Linux, and I don't know why.
    # It seems that the callback function is called, but the
    # parameters are not passed correctly.  The test passes on
    # Windows and 64-bit OSX.
    #
    # The problem is
