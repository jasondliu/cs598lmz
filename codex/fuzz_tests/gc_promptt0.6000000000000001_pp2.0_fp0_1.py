import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() and gc.collect(2)
# Also test gc.get_referrers()

# Collectable objects
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

class E(A):
    pass

class F(E):
    pass

class G(A):
    pass

class H(G):
    pass

class I(A):
    pass

class J(I):
    pass

class K(I):
    pass

class L(I):
    pass

class M(K, J, L):
    pass

class N:
    pass

class O(N):
    pass

class P(N):
    pass

class Q(N):
    pass

class R(O):
    pass

class S(O):
    pass

class T(P):
    pass

class U(P):
    pass

class V(Q):
    pass

class W(Q
