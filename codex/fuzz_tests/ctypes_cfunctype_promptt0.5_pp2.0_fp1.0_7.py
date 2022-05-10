import ctypes
# Test ctypes.CFUNCTYPE

# Test calling a function pointer
#
# NOTE: this test is NOT run by default.  To run it,
# edit the Makefile and change the line:
#
# TEST_CFLAGS = -DTEST_RUN_CTYPES_CFUNCTYPE
#
# to:
#
# TEST_CFLAGS = -DTEST_RUN_CTYPES_CFUNCTYPE=1
#
# and then run 'make test'.

import _ctypes_test

libc = ctypes.CDLL(_ctypes_test.__file__)

f = libc.fp
f.restype = ctypes.c_int
f.argtypes = (ctypes.c_int, ctypes.c_int)

if f(5, 6) != 11:
    raise RuntimeError("fp(5, 6) returned %d, instead of 11" % f(5, 6))

# Test calling a function pointer stored as attribute
# of a ctypes instance

class X(ctypes.Structure):
    _fields_ = [("fp
