import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()

# Test gc.get_threshold()
gc.get_threshold()

# Test gc.set_threshold()
gc.set_threshold(700, 10, 10)
gc.get_threshold()

# Test gc.get_count()
gc.get_count()

# Test gc.get_stats()
gc.get_stats()

# Test gc.garbage
gc.garbage

# Test gc.is_tracked()
gc.is_tracked(gc.garbage[0])

# Test gc.get_referrers()
gc.get_referrers(gc.garbage[0])

# Test gc.get_referents()
gc.get_referents(gc.garbage[0])

# Test gc.DEBUG_STATS
gc.DEBUG_STATS

# Test gc.DEBUG_LEAK
gc.DEBUG_LEAK

# Test gc.DEBUG_COLLECTABLE
gc.DEBUG_COLLECTABLE

# Test
