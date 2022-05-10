import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()

# Test gc.garbage
gc.garbage

# Test gc.get_count()
gc.get_count()

# Test gc.get_debug()
gc.get_debug()

# Test gc.get_objects()
gc.get_objects()

# Test gc.get_referrers()
gc.get_referrers()

# Test gc.get_threshold()
gc.get_threshold()

# Test gc.set_debug()
gc.set_debug(gc.DEBUG_COLLECTABLE)

# Test gc.set_threshold()
gc.set_threshold(1000, 10, 10)

# Test gc.is_tracked()
gc.is_tracked(1)

# Test gc.is_finalized()
gc.is_finalized(1)

# Test gc.get_referents()
gc.get_referents(1)

# Test gc.get_referrers()
gc.get_re
