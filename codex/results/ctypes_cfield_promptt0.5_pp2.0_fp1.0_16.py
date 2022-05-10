import ctypes
# Test ctypes.CField
class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

class RECT(ctypes.Structure):
    _fields_ = [("left", ctypes.c_int),
                ("top", ctypes.c_int),
                ("right", ctypes.c_int),
                ("bottom", ctypes.c_int)]

class NESTED(ctypes.Structure):
    _fields_ = [("point", POINT),
                ("rect", RECT)]


class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

class D(ctypes.Structure):
    _fields_ = [("b", ctypes.c_int),
                ("c", C)]

class E(ctypes.Structure):
    _fields_ = [("d", D),
                ("e", ctypes.c_int)]

class F(ctypes.Structure):
    _fields_ = [("
