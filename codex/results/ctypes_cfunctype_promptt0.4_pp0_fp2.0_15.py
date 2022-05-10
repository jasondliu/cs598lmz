import ctypes
# Test ctypes.CFUNCTYPE

if sys.platform == 'win32':
    import _ctypes_test
    dll = ctypes.CDLL(_ctypes_test.__file__)
else:
    dll = ctypes.CDLL(None)

# XXX this is not working on 64-bit windows
# XXX this is not working on 64-bit linux

# The following function is defined in _ctypes_test.c:
#
# int add(int a, int b) {
#     return a+b;
# }

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

class X(ctypes.Structure):
    _fields_ = [("n", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("n", ctypes.c_int)]

add = dll._testfunc_add
add.argtypes = (ctypes.c_int, ctypes.c_int)
add.restype = ctypes
