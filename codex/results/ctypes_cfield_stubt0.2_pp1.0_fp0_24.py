import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class D(C):
    pass

class E(D):
    _fields_ = [('y', ctypes.c_int)]

class F(E):
    _fields_ = [('z', ctypes.c_int)]

class G(F):
    pass

class H(G):
    _fields_ = [('a', ctypes.c_int)]

class I(H):
    _fields_ = [('b', ctypes.c_int)]

class J(I):
    _fields_ = [('c', ctypes.c_int)]

class K(J):
    pass

class L(K):
    _fields_ = [('d', ctypes.c_int)]

class M(L):
    _fields_ = [('e', ctypes.c_int)]

class N(M):
    _fields_ = [('f', ctypes.c_int)]

class O(
