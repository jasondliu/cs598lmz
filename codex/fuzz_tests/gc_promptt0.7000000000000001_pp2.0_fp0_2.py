import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect
# Note that collect() > 0 does not mean that all uncollectable objects have been collected.
# To test for true liveness, you can use the is_live() method of the gc module.
#
# This example creates a pair of cycles with one object per cycle, so you know that
# the objects were not collected because they were involved in a larger cycle.

class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)
b = A(20)
a.other = b
b.other = a
A.__init__.__code__ = weakref.ref(b)
b.__code__ = weakref.ref(A.__init__.__code__)

# Now a and b are uncollectable, but their refcounts are 1, so
# the following does nothing:
del a, b
gc.collect()
print(gc.is_tracked(A.__init__.__code__)) # True
gc.collect
