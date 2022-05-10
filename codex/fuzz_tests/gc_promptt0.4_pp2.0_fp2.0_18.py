import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#
# This test is not very reliable, since it depends on the exact order
# of the weakref callbacks.  However, it is better than nothing.

# This test is not very reliable, since it depends on the exact order
# of the weakref callbacks.  However, it is better than nothing.

class C(object):
    pass

# Create a cycle that is not collectable when the test starts
c = C()
c.cycle = c
w = weakref.ref(c)

# Enter an uncollectable cycle, and check that it gets collected
# anyway.
l = []
l.append(l)
del l
gc.collect()

# Check that the object is gone
assert w() is None
