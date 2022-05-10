import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class D(C):
    _fields_ = [('y', ctypes.c_int)]

class E(C):
    _fields_ = [('y', ctypes.c_int)]

class F(D, E):
    _fields_ = [('z', ctypes.c_int)]

class G(D, E):
    _fields_ = [('z', ctypes.c_int)]

class H(F, G):
    _fields_ = [('w', ctypes.c_int)]

class I(H):
    _fields_ = [('w', ctypes.c_int)]

class J(H):
    _fields_ = [('w', ctypes.c_int)]

class K(I, J):
    pass

class L(J, I):
    pass

class M(K, L):
    pass

class N(L, K):
    pass

class O(
