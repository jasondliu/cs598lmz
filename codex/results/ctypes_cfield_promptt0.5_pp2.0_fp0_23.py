import ctypes
# Test ctypes.CField

class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

class D(C):
    _fields_ = [("b", ctypes.c_int)]

class E(D):
    _fields_ = [("c", ctypes.c_int)]

class F(E):
    _fields_ = [("d", ctypes.c_int)]

class G(F):
    _fields_ = [("e", ctypes.c_int)]

class H(G):
    _fields_ = [("f", ctypes.c_int)]

class I(H):
    _fields_ = [("g", ctypes.c_int)]

class J(I):
    _fields_ = [("h", ctypes.c_int)]

class K(J):
    _fields_ = [("i", ctypes.c_int)]

class L(K):
    _fields_ = [("j", ctypes.c_int)]

class M(L):
    _fields_
