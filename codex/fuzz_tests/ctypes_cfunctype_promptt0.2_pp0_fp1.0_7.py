import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

#
# The rest of the file is a modified copy of _ctypes_test.c
#

#
# Test CFUNCTYPE(c_int, c_int)
#

f = lib.int_to_int
f.restype = ctypes.c_int
f.argtypes = (ctypes.c_int,)

for i in range(100):
    assert f(i) == i*2

#
# Test CFUNCTYPE(c_int, c_int, c_int)
#

f = lib.int_to_int_to_int
f.restype = ctypes.c_int
f.argtypes = (ctypes.c_int, ctypes.c_int)

for i in range(100):
    for j in range(100):
        assert f(i, j) == i*2 + j*3

#
# Test CFUNCTYPE(c_int,
