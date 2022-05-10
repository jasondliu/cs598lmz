import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

class E(D):
    pass

class F(D):
    pass

class G(E, F):
    pass

class H(G):
    pass

class I(G):
    pass

class J(H, I):
    pass

class K(J):
    pass

class L(J):
    pass

class M(K, L):
    pass

class N(M):
    pass

class O(M):
    pass

class P(N, O):
    pass

class Q(P):
    pass

class R(P):
    pass

class S(Q, R):
    pass

class T(S):
    pass

class U(S):
    pass

class V(T, U):
    pass

class W(V):
    pass

class X(V):

