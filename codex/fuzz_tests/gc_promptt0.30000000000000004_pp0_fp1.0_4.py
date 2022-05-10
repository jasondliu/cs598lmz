import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()

# Test gc.get_threshold()
gc.get_threshold()

# Test gc.set_threshold()
gc.set_threshold(1, 2, 3)
gc.set_threshold(1, 2)
gc.set_threshold(1)

# Test gc.get_count()
gc.get_count()

# Test gc.get_stats()
gc.get_stats()

# Test gc.set_debug()
gc.set_debug(gc.DEBUG_STATS)
gc.set_debug(gc.DEBUG_LEAK)
gc.set_debug(0)

# Test gc.get_objects()
gc.get_objects()

# Test gc.get_referrers()
gc.get_referrers(gc)

# Test gc.get_referents()
gc.get_referents(gc)

# Test gc.is_tracked()
gc.is_tracked(gc)

# Test gc.garbage
