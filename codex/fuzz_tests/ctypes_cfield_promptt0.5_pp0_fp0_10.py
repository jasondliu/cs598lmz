import ctypes
# Test ctypes.CField

class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

class D(C):
    _fields_ = [("b", ctypes.c_long)]

class E(C):
    _fields_ = [("c", ctypes.c_short)]

class F(D, E):
    _fields_ = [("d", ctypes.c_char)]

class G(F):
    _fields_ = [("e", ctypes.c_char)]

class H(G):
    _fields_ = [("f", ctypes.c_char)]

class I(H):
    _fields_ = [("g", ctypes.c_char)]

class J(I):
    _fields_ = [("h", ctypes.c_char)]

class K(J):
    _fields_ = [("i", ctypes.c_char)]

class L(K):
    _fields_ = [("j", ctypes.c_char)]

class M(L):
    _
