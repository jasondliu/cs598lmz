import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()

# Check for collectable objects
assert gc.collect() == 0

# No collectable objects
assert gc.collect() == 0

# Add a cyclic trash object
l = []
l.append(l)
assert gc.collect() == 1

# Now there are no collectable objects
assert gc.collect() == 0

# Add another cyclic trash object
l = []
l.append(l)
assert gc.collect() == 1

# Add a trash object that isn't cyclic
l = []
assert gc.collect() == 1

# Check for collectable objects
assert gc.collect() == 0

# Add a cyclic trash object
l = []
l.append(l)
assert gc.collect() == 1

# Add a trash object that isn't cyclic
l = []
assert gc.collect() == 1

# Check for collectable objects
assert gc.collect() == 0

# Add a cyclic trash object
l = []
l.append(l)
assert gc.collect
