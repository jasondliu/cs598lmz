import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs

# Create a list of objects and weakrefs to them
n = 100
objects = [C() for i in range(n)]
refs = [weakref.ref(obj) for obj in objects]

# Clear references
objects = refs = None

# Collect!  (should clear the list)
gc.collect()

# Verify that the list is really gone
assert len(gc.garbage) == 0, gc.garbage
# Test gc.collect() with weakrefs and callbacks

class C:
    pass

class D:
    pass

# Create a list of objects and weakrefs to them
n = 100
objects = [C() for i in range(n)]
refs = [weakref.ref(obj, lambda wr: D()) for obj in objects]

# Clear references
objects = refs = None

# Collect!  (should clear the list)
gc.collect()

# Verify that the list is really gone
assert len(gc.garbage) == 0, gc.garbage
# Test gc.
