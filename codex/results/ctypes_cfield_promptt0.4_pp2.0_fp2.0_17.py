import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("y", ctypes.c_int)]

class Z(ctypes.Structure):
    _fields_ = [("x", X),
                ("y", Y)]

class XX(ctypes.Structure):
    _fields_ = [("z", Z),
                ("x", X)]

class XY(ctypes.Structure):
    _fields_ = [("x", X),
                ("y", Y)]

class ZZ(ctypes.Structure):
    _fields_ = [("x", X),
                ("y", Y),
                ("z", Z)]

class XXX(ctypes.Structure):
    _fields_ = [("x", X),
                ("y", Y),
                ("z", Z),
                ("w", X)]

class XXY(ctypes.Structure):
    _fields_ = [("x", X),
                ("y
