import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    _fields_ = [("x", ctypes.c_int)]

class C(object):
    x = ctypes.c_int
    _fields_ = [("x", ctypes.c_int)]

class D(C):
    y = ctypes.c_int
    _fields_ = [("y", ctypes.c_int)]

class E(D):
    z = ctypes.c_int
    _fields_ = [("z", ctypes.c_int)]

class F(E):
    pass

class G(F):
    pass

class H(G):
    pass

class I(H):
    pass

class J(I):
    pass

class K(J):
    pass

class L(K):
    pass

class M(L):
    pass

class N(M):
    pass

class O(N):
    pass

class P(O):
    pass

class Q(P):
    pass

class R(Q):
    pass
