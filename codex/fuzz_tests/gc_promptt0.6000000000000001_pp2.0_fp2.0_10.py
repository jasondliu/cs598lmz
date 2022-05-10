import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() after uncollectable objects have been created.
# This tests that collect() returns the correct number of objects
# collected and uncollectable.

gc.collect()
a = []
a.append(a)
b = []
b.append(b)
# There are now two uncollectable objects.
gc.collect()
assert gc.collect() == 2
assert gc.collect() == 0

# This time make one object uncollectable, then make it collectable
# again.

gc.collect()
a = []
a.append(a)
b = []
b.append(b)
gc.collect()
assert gc.collect() == 2
a = None
gc.collect()
assert gc.collect() == 1
assert gc.collect() == 0

# Now make sure that gc.collect() doesn't collect things in the wrong
# order.

gc.collect()
a = []
w = weakref.ref(a)
a.append(a)
b = []
b.append(b)
gc.collect()
assert gc.collect
