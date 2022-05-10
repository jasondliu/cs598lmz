import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#
# This test is a bit tricky because we want to test that the
# collect() function works, but we don't want to depend on the
# collect() function to make the test pass.  The trick is to
# create a cycle that will be collected, but to break the cycle
# before the test is complete, so that we are still holding
# references to the objects at the end of the test.
#
# The cycle is created by creating a list L whose only element is
# L itself.  To break the cycle, we replace L[0] with None after
# creating the cycle.

# Create a list L whose only element is L itself.
L = []
L.append(L)

# Record the number of objects known to the gc pre-cycle.
n0 = len(gc.get_objects())

# Create a cycle and don't break it.
x = []
x.append(x)

# Record the number of objects known to the gc pre-collection.
n1 = len(gc.get_objects())

# Collect and record the number of objects known to the g
