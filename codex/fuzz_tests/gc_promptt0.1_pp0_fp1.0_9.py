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

for c in [A, B, C, D]:
    a = c()
    a = None
    gc.collect()

# Test gc.get_referrers()

a = A()
b = B()
c = C()
d = D()

a.attr = a
b.attr = b
c.attr = c
d.attr = d

a.attr = b
b.attr = c
c.attr = d
d.attr = a

a.attr = c
b.attr = d
c.attr = a
d.attr = b

a.attr = d
b.attr = a
c.attr = b
d.attr = c

a.attr = None
b.attr = None
c.attr = None
d.attr = None

a = None
b = None
c = None
d = None

gc.collect()
