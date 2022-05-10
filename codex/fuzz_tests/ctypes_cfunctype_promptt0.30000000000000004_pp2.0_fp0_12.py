import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

class Z(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

Xp = ctypes.POINTER(X)
Yp = ctypes.POINTER(Y)
Zp = ctypes.POINTER(Z)

# XXX This is a hack.  We need to find a way to get the calling
# convention used by the compiler...
if ctypes.sizeof(ctypes.c_int) == ctypes.sizeof(ctypes.c_void_p):
    CDLL = ctypes.CDLL
else:
    CDLL = ctypes.WinDLL

# XXX This is a hack.  We need to find a way to get the calling
# convention used
