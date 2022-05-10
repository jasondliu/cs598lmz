import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

#
# Test that CFUNCTYPE(None) works

f = ctypes.CFUNCTYPE(None)(lib.identity)
f()

#
# Test that CFUNCTYPE(None, None) works

f = ctypes.CFUNCTYPE(None, None)(lib.identity)
f()

#
# Test that CFUNCTYPE(None, c_int) works

f = ctypes.CFUNCTYPE(None, ctypes.c_int)(lib.identity)
f(42)

#
# Test that CFUNCTYPE(c_int, c_int) works

f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lib.identity)
assert f(42) == 42

#
# Test that CFUNCTYPE(c_int, c_int, c_int) works

f = ctypes
