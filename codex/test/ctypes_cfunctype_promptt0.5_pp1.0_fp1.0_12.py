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
