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

lib.set_callback.restype = Xp
lib.set_callback.argtypes = (ctypes.c_int, CALLBACKFUNC, ctypes.c_int)

lib.use_callback.restype = ctypes.c_int
lib.use_callback.argtypes = (Xp, ctypes.c_int)

lib.free_callback.argtypes = (Xp,)

x = lib.set_callback(1, CALLBACKFUNC(callback), 0)
assert lib.use_callback(x, 3) == 6
lib.free_
