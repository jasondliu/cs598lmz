import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs

# Create a list of objects
L = [weakref.ref(object()) for i in range(10)]

# Collect all garbage
gc.collect()

# Check that the list is empty
assert len(L) == 0
