import ctypes
# Test ctypes.CFUNCTYPE
#
# This test is used to determine whether the compiler is capable of
# generating the correct function type for CFUNCTYPE.  This is used to
# determine whether the tests for calling functions with the 'f' code
# should be skipped.

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(("f", lib))

if f(1, 2) != 3:
    raise RuntimeError, "CFUNCTYPE(c_int, c_int, c_int)(('f', lib)) failed"

f = ctypes.CFUNCTYPE(ctypes.c_int,
                     ctypes.c_int, ctypes.c_int,
                     ctypes.c_int, ctypes.c_int)(("f", lib))

if f(1, 2, 3, 4) != 10:
    raise RuntimeError, "CFUNCTYPE(c_int
