import ctypes
# Test ctypes.CField filledup by types.Member()
import _ctypes_test
lib = ctypes.CDLL(_ctypes_test.__file__)
try:
    lib.myfunc.argtypes = (ctypes.c_char,)
except TypeError as e:
    print(e)

class X(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int)]

lib.myfunc.argtypes = (X,)
try:
    lib.myfunc.argtypes = (ctypes.c_int,)
except TypeError as e:
    print(e)
#
# Test that member names with leading underscores can't get access
# by attribute lookup.
#
lib.test2.argtypes = []
lib.test2.restype = ctypes.c_int
try:
    a=lib.test2._internal
except AttributeError as e: # "attribute name must not start with '_'"
    print(e)

#
# Test alignment of members (see SF projectzilla bug #2894712)
#
class TestBug2894712
