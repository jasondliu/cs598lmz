import ctypes
# Test ctypes.CField

class S(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class T(ctypes.Structure):
    _fields_ = [("s", S),
                ("c", ctypes.c_char)]

class U(ctypes.Structure):
    _fields_ = [("t", T),
                ("d", ctypes.c_double)]

class V(ctypes.Structure):
    _fields_ = [("u", U),
                ("e", ctypes.c_longlong)]

class W(ctypes.Structure):
    _fields_ = [("v", V),
                ("f", ctypes.c_longlong)]

class X(ctypes.Structure):
    _fields_ = [("w", W),
                ("g", ctypes.c_longlong)]

class Y(ctypes.Structure):
    _fields_ = [("x", X),
                ("h", ctypes.c_longlong)]


