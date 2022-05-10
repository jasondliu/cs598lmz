import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 0

class A(object):
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
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

class Q(P):
    pass

class R(Q):
    pass

class S(R):
    pass

class T(S):
    pass

class U(T):
    pass

class V(U):
    pass

class W(V):
    pass

class X(W):
    pass

class Y(X):
    pass
