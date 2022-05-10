import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class A:
    pass

class B(A):
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

for c in [A, B, C, D, E, F, G, H]:
    a = c()
    a = None
    gc.collect()

# Test gc.get_referrers()

a = A()
b = B()
c = C()
d = D()

e = E()
f = F()
g = G()
h = H()

# Test gc.get_referents()

a = A()
b = B()
c = C()
d = D()

e = E()
f = F()
g = G()
h = H()

# Test gc.get_objects()

a = A()
b = B()
