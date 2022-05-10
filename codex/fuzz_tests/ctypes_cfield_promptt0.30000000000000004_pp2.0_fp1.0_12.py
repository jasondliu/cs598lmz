import ctypes
# Test ctypes.CField

class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]
    _anonymous_ = ("b",)

class D(C):
    _fields_ = [("c", ctypes.c_int)]

class E(D):
    _fields_ = [("d", ctypes.c_int)]

class F(C):
    _fields_ = [("c", ctypes.c_int)]

class G(C):
    _fields_ = [("b", ctypes.c_int),
                ("c", ctypes.c_int)]

class H(C):
    _fields_ = [("b", ctypes.c_int),
                ("c", ctypes.c_int),
                ("d", ctypes.c_int)]

class I(C):
    _fields_ = [("c", ctypes.c_int),
                ("d", ctypes.c_int)]

class J(C):
    _fields_ =
