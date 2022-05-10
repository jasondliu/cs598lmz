import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class A:
    pass

class B:
    pass

class C(A):
    pass

class D(B, C):
    pass

class E(object):
    pass

class F(E):
    pass

class G(E):
    pass

class H(F, G):
    pass

class I(H):
    pass

class J(I):
    pass

class K(I):
    pass

class L(J, K):
    pass

class M(L):
    pass

a = A()
b = B()
c = C()
d = D()
e = E()
f = F()
g = G()
h = H()
i = I()
j = J()
k = K()
l = L()
m = M()

# Collecting a reference cycle with two collectable objects
# in it should free both objects.
a.b = b
b.a = a
gc.collect()
assert gc.collect() == 2

# Collecting a reference cycle
