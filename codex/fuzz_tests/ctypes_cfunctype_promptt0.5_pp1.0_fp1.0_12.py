import ctypes
# Test ctypes.CFUNCTYPE
import _ctypes_test

OpaquePointer = ctypes.c_void_p

lib = ctypes.CDLL(_ctypes_test.__file__)

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("b", ctypes.c_int)]

class Z(ctypes.Structure):
    _fields_ = [("c", ctypes.c_int)]

# The function returns a pointer to X, and receives a pointer to Y
f = lib.my_callback
f.restype = ctypes.POINTER(X)
f.argtypes = [ctypes.POINTER(Y)]

# This is the function to be called from the C code
def callback(arg):
    print(arg.contents.b)
    return X(arg.contents.b * 2)

# The C code calls the function "callback" which returns a pointer to X
# and receives a pointer to Y.  The callback
