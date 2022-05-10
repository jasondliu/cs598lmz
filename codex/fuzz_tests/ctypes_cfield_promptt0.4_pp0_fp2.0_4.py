import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("x", X)]

class Z(ctypes.Structure):
    _fields_ = [("y", Y)]

class W(ctypes.Structure):
    _fields_ = [("z", Z)]

class V(ctypes.Structure):
    _fields_ = [("w", W)]

class U(ctypes.Structure):
    _fields_ = [("v", V)]

class T(ctypes.Structure):
    _fields_ = [("u", U)]

class S(ctypes.Structure):
    _fields_ = [("t", T)]

class R(ctypes.Structure):
    _fields_ = [("s", S)]

class Q(ctypes.Structure):
    _fields_ = [("r", R)]

class P(ctypes.St
