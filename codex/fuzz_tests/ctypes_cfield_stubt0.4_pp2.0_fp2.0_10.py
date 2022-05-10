import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

# Test a simple case:
class X(object):
    def __init__(self, x):
        self.x = x

class Y(X):
    def __init__(self, x):
        X.__init__(self, x)

class Z(Y):
    def __init__(self, x):
        Y.__init__(self, x)

class A(Z):
    pass

class B(A):
    pass

class C(B):
    pass

class D(C):
    pass

class E(D):
    pass

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

class
