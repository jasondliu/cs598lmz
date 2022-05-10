import ctypes
# Test ctypes.CField

class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class D(C):
    _fields_ = [("c", ctypes.c_int)]

class E(C):
    _fields_ = [("b", ctypes.c_int, 1)]

class F(C):
    _fields_ = [("b", ctypes.c_int, 1),
                ("c", ctypes.c_int)]

class G(C):
    _fields_ = [("c", ctypes.c_int),
                ("b", ctypes.c_int, 1)]

class H(C):
    _fields_ = [("c", ctypes.c_int),
                ("b", ctypes.c_int, 1),
                ("d", ctypes.c_int)]

class I(C):
    _fields_ = [("c", ctypes.c_int),
                ("b", ctypes.c_int, 1),
               
