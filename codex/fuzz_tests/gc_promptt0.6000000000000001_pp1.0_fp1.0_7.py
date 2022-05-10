import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() doesn't crash
gc.collect()
# Test gc.collect() doesn't crash
gc.collect()

# Create a cycle to make sure the collector finds it
a = []
b = [a, a]
a.append(b)
del a, b
gc.collect()

# Check that we can flush the collector's internal buffers
# before doing a collect.
gc.collect()

# Check that we can flush the collector's internal buffers
# before doing a collect.
gc.collect()

# Check that we can flush the collector's internal buffers
# before doing a collect.
gc.collect()

# Check that we can flush the collector's internal buffers
# before doing a collect.
gc.collect()

# Check that we can flush the collector's internal buffers
# before doing a collect.
gc.collect()

# Check that we can flush the collector's internal buffers
# before doing a collect.
gc.collect()

# Check that we can flush the collector's internal buffers
# before doing a collect.
gc.collect()

# Check that we can flush the collector's internal buffers
