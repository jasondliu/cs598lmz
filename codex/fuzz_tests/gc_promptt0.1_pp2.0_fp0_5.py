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

a = A()
b = B()
c = C()
d = D()
e = E()

# Create a reference cycle
a.x = b
b.x = c
c.x = d
d.x = e
e.x = a

# Create a weakref to the cycle
wr = weakref.ref(a)

# Collect
gc.collect()

# Check that the weakref is dead
assert wr() is None

# Check that the objects are dead
assert gc.is_tracked(a)
assert gc.is_tracked(b)
assert gc.is_tracked(c)
assert gc.is_tracked(d)
assert gc.is_tracked(e)

# Check that the objects are collectable
assert gc.is_collectable(a)

