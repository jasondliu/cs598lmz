import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("x", X),
                ("y", X)]

class Z(ctypes.Structure):
    _fields_ = [("y", Y),
                ("z", Y)]

class W(ctypes.Structure):
    _fields_ = [("x", X),
                ("y", Y),
                ("z", Z)]

class V(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.c_int)]
    _anonymous_ = ["b"]

class U(ctypes.Structure):
    _fields_ = [("x", V),
                ("y", V),
                ("z", V)]

class T(ctypes.
