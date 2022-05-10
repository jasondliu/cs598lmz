import ctypes
# Test ctypes.CFUNCTYPE
prototype = ctypes.CFUNCTYPE( ctypes.c_int, ctypes.c_int, ctypes.c_int )
paramflags = ( 1, "a", 0 ), ( 1, "b", 0 )

import _ctypes_test
cb = prototype( _ctypes_test.callit, paramflags )

res = cb(3, 5)
if res != 8:
    raise RuntimeError, "Result should be 8, got %d" % res

# test that ctypes.pointer(x) returns the same object as ctypes.pointer(x)
import sys
if sys.version_info[0] > 2:
    bytes_t = bytes
else:
    bytes_t = str

lib = ctypes.CDLL(_ctypes_test.__file__)
f = lib.ptradd
f.restype = ctypes.c_void_p
f.argtypes = (ctypes.c_void_p, ctypes.c_int)

data = (ctypes.c_byte * 16)()
p1 = ctypes.
