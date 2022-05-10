import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    __slots__ = ['x']

class D(C):
    __slots__ = ['y']

class E(D):
    __slots__ = ['z']

class F(E):
    __slots__ = ['t']

class G(F):
    __slots__ = ['u']

class H(G):
    __slots__ = ['v']

class I(H):
    __slots__ = ['w']

class J(I):
    __slots__ = ['x']

class K(J):
    __slots__ = ['y']

class L(K):
    __slots__ = ['z']

class M(L):
    __slots__ = ['t']

class N(M):
    __slots__ = ['u']

class O(N):
    __slots__ = ['v']

class P(O):
    __slots__ = ['w']

class Q(P):
    __slots__ = ['x']
