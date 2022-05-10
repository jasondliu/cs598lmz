import ctypes
# Test ctypes.CFUNCTYPE
import _ctypes_test
lib = ctypes.CDLL(_ctypes_test.__file__)

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

Xp = ctypes.POINTER(X)
NULL = ctypes.c_void_p()

def callback(x):
    return 2*x.a

CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, X)

