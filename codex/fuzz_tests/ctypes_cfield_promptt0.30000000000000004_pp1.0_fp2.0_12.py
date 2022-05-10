import ctypes
# Test ctypes.CField

class C(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int)]
    _anonymous_ = ["x"]

class D(C):
    _fields_ = [("y", ctypes.c_int)]

class E(D):
    _fields_ = [("z", ctypes.c_int)]

class F(E):
    _fields_ = [("w", ctypes.c_int)]

class G(F):
    _fields_ = [("a", ctypes.c_int)]

class H(G):
    _fields_ = [("b", ctypes.c_int)]

class I(H):
    _fields_ = [("c", ctypes.c_int)]

class J(I):
    _fields_ = [("d", ctypes.c_int)]

class K(J):
    _fields_ = [("e", ctypes.c_int)]

class L(K):
    _fields_ = [("f", ctypes.c_int)]


