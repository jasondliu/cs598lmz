import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with no args.
gc.collect()
# Test gc.collect() with an arg.
gc.collect(2)
# Verify that gc.DEBUG_COLLECTABLE is set.
gc.get_debug() & gc.DEBUG_COLLECTABLE
# Verify that gc.DEBUG_COLLECTABLE is not set.
gc.set_debug(0)
gc.get_debug() & gc.DEBUG_COLLECTABLE
# Create a list of objects to be collected.
collected = [Cycle(i) for i in range(10)] + \
            [Weak(Cycle(i)) for i in range(10)]

# Verify that gc.DEBUG_COLLECTABLE is set.
gc.set_debug(gc.DEBUG_COLLECTABLE)

# Collect the objects.
gc.collect()

# Verify that the objects have been collected.
for o in collected:
    assert o.ref() is None
    assert o.weakref() is None
# Test gc.garbage.
gc.garbage
# Test gc.get_threshold().
gc.
