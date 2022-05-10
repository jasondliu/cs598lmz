import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#
# Test that gc.collect() collects unreachable objects.
#
# The test also checks that gc.collect() is implemented correctly in
# the sense that it doesn't collect reachable objects and that it
# collects enough unreachable objects in one go (some implementations
# of the Boehm GC are known to require multiple calls to gc.collect()
# to collect all unreachable objects).

# Create a reachable object
l = [1, 2, 3]

# Create a bunch of unreachable objects
for i in xrange(100):
    _ = []
    for j in xrange(100):
        _.append(j)

# Check that gc.collect() collects unreachable objects, and that it
# doesn't collect reachable objects.

gc.collect()
assert gc.collect() == 0
assert gc.collect() == 0

# Create an object with a finalizer
class C:
    def __del__(self):
        pass

c = C()

# Check that gc.collect() collects objects with finalizers
del c
gc.
