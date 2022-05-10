import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()

# Test gc.get_referrers()
gc.get_referrers(None)

# Test gc.get_referents()
gc.get_referents(None)

# Test gc.get_objects()
gc.get_objects()

# Test gc.get_stats()
gc.get_stats()

# Test gc.get_threshold()
gc.get_threshold()

# Test gc.set_threshold()
gc.set_threshold(1, 1, 1)

# Test gc.is_tracked()
gc.is_tracked(None)

# Test gc.is_finalized()
gc.is_finalized(None)

# Test gc.garbage
gc.garbage

# Test gc.set_debug()
gc.set_debug(gc.DEBUG_STATS)
gc.set_debug(gc.DEBUG_COLLECTABLE)
gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
gc.set_
