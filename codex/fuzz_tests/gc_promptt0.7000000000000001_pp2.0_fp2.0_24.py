import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() when an object is involved in a cycle,
# but some of the objects in the cycle are weakly referenced.
# The cycle should be collectable even though there are weakrefs
# in the cycle.

class A:
    pass

a = A()
a.b = A()
a.b.a = a

a_wr = weakref.ref(a)
a.b_wr = weakref.ref(a.b)

del a
del a.b

# Verify that a and a.b are part of a reference cycle.
import gc
assert gc.collect() == 2

# Verify that the reference cycle is collectable.
assert gc.collect() == 1

# Verify that a_wr and a.b_wr are dead.
assert a_wr() is None
assert a.b_wr() is None

# Verify that the reference cycle is collectable.
assert gc.collect() == 0
