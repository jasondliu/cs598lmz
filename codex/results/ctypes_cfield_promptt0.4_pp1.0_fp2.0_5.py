import ctypes
# Test ctypes.CField.from_address

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("x", X),
                ("y", ctypes.c_int)]

class Z(ctypes.Structure):
    _fields_ = [("i", ctypes.c_int)]

class W(ctypes.Structure):
    _fields_ = [("i", ctypes.c_int),
                ("j", ctypes.c_int)]

class V(ctypes.Structure):
    _fields_ = [("w", W),
                ("z", Z)]

class U(ctypes.Structure):
    _fields_ = [("v", V),
                ("y", Y)]

class S(ctypes.Structure
