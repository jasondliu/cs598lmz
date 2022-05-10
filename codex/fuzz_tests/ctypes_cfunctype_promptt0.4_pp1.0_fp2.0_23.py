import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

Xp = ctypes.POINTER(X)

for tp in [ctypes.c_int,
           ctypes.c_void_p,
           X,
           Xp]:
    for restype in [ctypes.c_int,
                    ctypes.c_void_p,
                    X,
                    Xp]:
        for argtypes in [[],
                         [ctypes.c_int],
                         [ctypes.c_void_p],
                         [X],
                         [Xp],
                         [ctypes.c_int, ctypes.c_void_p],
                         [ctypes.c_int, X],
                         [ctypes.c_int, Xp],
                         [ctypes.c_void_p, ctypes.c_int],
                         [
