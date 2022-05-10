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

class E:
    pass

for c in [A, B, C, D, E]:
    a = c()
    a.a = a
    del a

gc.collect()
gc.collect()

# Test gc.get_referrers()

a = A()
b = B()
c = C()
d = D()
e = E()

a.a = a
b.a = b
c.a = c
d.a = d
e.a = e

a.b = b
b.a = a
b.b = b
b.c = c
b.d = d
b.e = e

a.c = c
c.a = a
c.b = b
c.c = c
c.d = d
c.e = e

a.d = d
d.a = a
d.b =
