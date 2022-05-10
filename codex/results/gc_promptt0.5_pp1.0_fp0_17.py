import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs

class A(object):
    pass

a = A()
wr = weakref.ref(a)

gc.collect()

# No refs to a left, it should be collected
gc.collect()
assert wr() is None

# No refs to a left, it should be collected
gc.collect()
assert wr() is None

# No refs to a left, it should be collected
gc.collect()
assert wr() is None
