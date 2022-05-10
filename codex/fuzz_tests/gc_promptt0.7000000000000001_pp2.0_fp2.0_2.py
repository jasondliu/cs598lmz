import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() on weakrefs
# Verify that a collectable object is not collected if it can be reached via a
# weakref, and that it is collected even if it only can be reached by a
# weakref in a collectable object.

# Create a weakref to an object that is not yet collectable, verify that
# gc.collect() doesn't collect it, and that it doesn't become collectable.
class A:
    pass

a = A()
a_wr = weakref.ref(a)

gc.collect()
assert not gc.is_tracked(a_wr)
assert not gc.is_tracked(a)
del a_wr
gc.collect()
assert not gc.is_tracked(a_wr)
assert not gc.is_tracked(a)

# Create a weakref to an object that is not yet collectable, verify that
# gc.collect() doesn't collect it, and that it does become collectable.
class A:
    pass

a = A()
a_wr = weakref.ref(a)
del
