import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("x", X),
                ("y", X)]

class Z(ctypes.Structure):
    _fields_ = [("y", Y),
                ("z", Y)]

class W(ctypes.Structure):
    _fields_ = [("z", Z),
                ("w", Z)]

class V(ctypes.Structure):
    _fields_ = [("w", W),
                ("v", W)]

class U(ctypes.Structure):
    _fields_ = [("v", V),
                ("u", V)]

class T(ctypes.Structure):
    _fields_ = [("u", U),
                ("t", U)]

class S(ctypes.Structure):
    _fields_ = [("t", T),
                ("s", T)]

class R(ct
