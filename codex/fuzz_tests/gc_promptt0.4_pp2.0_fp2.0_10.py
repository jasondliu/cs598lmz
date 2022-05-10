import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() and gc.collect(1)

class A:
    pass

class B:
    pass

class C(A, B):
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

