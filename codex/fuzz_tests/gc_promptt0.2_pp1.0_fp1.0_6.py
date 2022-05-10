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

# Test gc.get_referents()

a = A()
b = B()
c = C()
d = D()

a.attr = a
b.attr = b
c.attr = c
d.attr = d

# Test gc.get_objects()

a = A()
b = B()
c = C()
d = D()

a.attr = a
b.attr = b
c.attr = c
d.attr = d

# Test gc.
