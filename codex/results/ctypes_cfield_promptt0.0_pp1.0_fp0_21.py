import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("x", X),
                ("y", ctypes.c_int)]

class Z(ctypes.Structure):
    _fields_ = [("y", Y),
                ("z", ctypes.c_int)]

class W(ctypes.Structure):
    _fields_ = [("z", Z),
                ("w", ctypes.c_int)]

class V(ctypes.Structure):
    _fields_ = [("w", W),
                ("v", ctypes.c_int)]

class U(ctypes.Structure):
    _fields_ = [("v", V),
                ("u", ctypes.c_int)]

class T(ctypes.Structure):
    _fields_ = [("u", U),
                ("t", ctypes.c_int)]

class S(ct
