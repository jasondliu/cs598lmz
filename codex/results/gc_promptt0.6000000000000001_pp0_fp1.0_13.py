import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#
# This is a test for bug #126435.
#
# Collectable objects are objects that are collectable but not uncollectable.
# They are objects that have a __del__ method, but not a __del__ method that
# calls gc.collect().

class C:
    def __init__(self, n):
        self.n = n
    def __repr__(self):
        return "<C %d>" % self.n
    def __del__(self):
        global n_deleted
        n_deleted += 1

# Create a bunch of objects.
for i in range(5):
    exec "c%d = C(i)" % i

gc.collect()
assert gc.collect() == 0

# Create a reference cycle.
c1.cycle = c2
c2.cycle = c1

# Create a bunch of other objects.
for i in range(5, 10):
    exec "c%d = C(i)" % i

# Delete c0.
del c0

# Collect.  We
