import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

gc.collect()

a = A()
b = B()
c = C()
d = D()

class E(D):
    pass

e = E()

class F(E):
    pass

f = F()

class G(F):
    pass

g = G()

class H(G):
    pass

h = H()

class I(H):
    pass

i = I()

class J(I):
    pass

j = J()

class K(J):
    pass

k = K()

class L(K):
    pass

l = L()

class M(L):
    pass

m = M()

class N(M):
    pass

n = N()

class O(N):
    pass

o = O()

class P(O
