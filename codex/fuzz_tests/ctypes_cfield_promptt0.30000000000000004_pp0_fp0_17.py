import ctypes
# Test ctypes.CField

class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_char),
                ("b", ctypes.c_int)]

class D(C):
    _fields_ = [("c", ctypes.c_char),
                ("d", ctypes.c_int)]

class E(D):
    _fields_ = [("e", ctypes.c_char),
                ("f", ctypes.c_int)]

class F(E):
    _fields_ = [("g", ctypes.c_char),
                ("h", ctypes.c_int)]

class G(F):
    _fields_ = [("i", ctypes.c_char),
                ("j", ctypes.c_int)]

class H(G):
    _fields_ = [("k", ctypes.c_char),
                ("l", ctypes.c_int)]

class I(H):
    _fields_ = [("m", ctypes.c_char),
                ("n", ctypes.c_int)]
