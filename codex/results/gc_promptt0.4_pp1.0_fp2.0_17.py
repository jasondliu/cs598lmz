import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()
gc.collect()
gc.collect()

# Test gc.garbage
gc.garbage

# Test gc.get_debug()
gc.get_debug()

# Test gc.get_threshold()
gc.get_threshold()

# Test gc.is_tracked()
gc.is_tracked(1)

# Test gc.set_debug()
gc.set_debug(gc.DEBUG_COLLECTABLE)
gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
gc.set_debug(gc.DEBUG_INSTANCES)
gc.set_debug(gc.DEBUG_OBJECTS)
gc.set_debug(gc.DEBUG_SAVEALL)
gc.set_debug(gc.DEBUG_LEAK)
gc.set_debug(gc.DEBUG_STATS)
gc.set_debug(0)

# Test gc.set_threshold()
gc.set_threshold(1, 2, 3)

# Test gc.get_count()
gc.
