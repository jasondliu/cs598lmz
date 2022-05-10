import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class D(C):
    _fields_ = [('y', ctypes.c_int)]

class E(D):
    _fields_ = [('z', ctypes.c_int)]

class F(E):
    _fields_ = [('w', ctypes.c_int)]

class G(F):
    _fields_ = [('w', ctypes.c_int)]

class H(G):
    _fields_ = [('w', ctypes.c_int)]

class I(H):
    _fields_ = [('w', ctypes.c_int)]

class J(I):
    _fields_ = [('w', ctypes.c_int)]

class K(J):
    _fields_ = [('w', ctypes.c_int)]

class L(K):
    _fields_ = [('w', ctypes.c_int)]

class M(L):
    _fields
