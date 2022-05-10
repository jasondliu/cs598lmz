import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() on a cyclic list with a weakref
# in the cycle.
# The weakref should be collected, the list not.
class A:
    pass

a = A()
a.x = [a]
w = weakref.ref(a)
del a
gc.collect()
gc.collect()
assert w() is None

class A:
    pass

a = A()
a.x = [a]
w = weakref.ref(a)
b = [a]
del a
gc.collect()
gc.collect()
assert w() is None
assert b[0] is b
