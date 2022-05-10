import ctypes
# Test ctypes.CField

class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class D(C):
    _fields_ = [("c", ctypes.c_int)]

class E(C):
    _fields_ = [("c", ctypes.c_int)]

class F(C):
    _fields_ = [("c", ctypes.c_int)]

class G(E):
    _fields_ = [("d", ctypes.c_int)]

class H(F):
    _fields_ = [("d", ctypes.c_int)]

class I(G, H):
    _fields_ = [("e", ctypes.c_int)]

class J(I):
    _fields_ = [("f", ctypes.c_int)]

class K(J):
    _fields_ = [("g", ctypes.c_int)]

class L(K):
    _fields_ = [("h", ctypes.c_
