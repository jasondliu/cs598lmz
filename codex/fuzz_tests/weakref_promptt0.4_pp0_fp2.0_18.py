import weakref
# Test weakref.ref() with a non-weakrefable object.
import _weakref

class C:
    pass

class D(C):
    pass

class E(D):
    pass

class F(D):
    pass

class G(F):
    pass

class H(F):
    pass

class I(G):
    pass

class J:
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

class Z(Y):
    pass

class AA
