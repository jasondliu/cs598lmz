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

# Make a cycle
a = A()
a.b = B()
a.c = C()
a.d = D()

a.b.a = a
a.c.a = a
a.d.a = a

a.b.b = a.b
a.c.c = a.c
a.d.d = a.d

a.b.c = a.c
a.b.d = a.d
a.c.b = a.b
a.c.d = a.d
a.d.b = a.b
a.d.c = a.c

# Make a reference to the cycle
wr = weakref.ref(a)

# Break the cycle
a = None

# Collect
gc.collect()

# Check the reference
assert wr() is None

# Check the debug flag
assert gc.get_debug
