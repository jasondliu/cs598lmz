import ctypes
# Test ctypes.CField
class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_char),
                ("b", ctypes.c_char),
                ("c", ctypes.c_short)]
    _pack_ = 1

class D(C):
    _fields_ = [("d", ctypes.c_int)]

class E(D):
    _fields_ = [("e", ctypes.c_longlong)]

class F(E):
    _fields_ = [("f", ctypes.c_double)]

class W(ctypes.Structure):
    _fields_ = [("a", ctypes.c_char),
                ("b", ctypes.c_char),
                ("c", ctypes.c_short),
                ("d", ctypes.c_int),
                ("e", ctypes.c_longlong),
                ("f", ctypes.c_double)]
    _pack_ = 1

class X(ctypes.Union):
    _fields_ = [("a", ctypes.c_char),
               
