import ctypes
# Test ctypes.CField
class C(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int)]

class D(C):
    _fields_ = [("y", ctypes.c_int)]

class E(D):
    _fields_ = [("z", ctypes.c_int)]

class F(E):
    _fields_ = [("t", ctypes.c_int)]

class G(F):
    _fields_ = [("s", ctypes.c_int)]

class H(G):
    _fields_ = [("r", ctypes.c_int)]

class I(H):
    _fields_ = [("q", ctypes.c_int)]

class J(I):
    _fields_ = [("p", ctypes.c_int)]

class K(J):
    _fields_ = [("o", ctypes.c_int)]

class L(K):
    _fields_ = [("n", ctypes.c_int)]

class M(L):
    _fields_ =
