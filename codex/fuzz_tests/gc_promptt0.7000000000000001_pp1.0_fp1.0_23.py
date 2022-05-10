import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() without objects being tracked
gc.collect()

# Test gc.collect() with objects being tracked

# Test gc.get_objects()

# Test gc.is_tracked()

# Test gc.garbage

# Test gc.get_count()

# Test gc.get_referrers()

# Test gc.get_referents()

# Test gc.DEBUG_STATS

# Test gc.DEBUG_LEAK

# Test gc.DEBUG_COLLECTABLE

# Test gc.DEBUG_UNCOLLECTABLE

# Test gc.DEBUG_INSTANCES

# Test gc.DEBUG_OBJECTS

# Test gc.DEBUG_SAVEALL

# Test gc.DEBUG_STATS

# Test gc.set_debug()
