import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect_generations()

# This test is a bit bogus.  It's hard to come up with a test that
# doesn't depend on the internal implementation details of the
# collector.  The best I could come up with was to make sure that
# collect_generations() doesn't collect more than it should.

# Create a bunch of objects that are one generation apart.
for i in range(10):
    exec('a%d = [None]' % i)

# Create a list of weak references to all the objects.
wr = []
for i in range(10):
    exec('wr.append(weakref.ref(a%d))' % i)

# Collect all generations up to and including 2.
gc.collect_generations(2)

# Check that objects in generations 3 and up are still alive.
for i in range(3, 10):
    if wr[i]() is None:
        print 'object in generation', i, 'was collected'

# Collect all generations up to and including 5.
gc.collect_generations(5)

# Check that objects in generations 6
