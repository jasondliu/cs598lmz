import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()
# Test gc.get_threshold()
gc.get_threshold()
# Test gc.set_threshold()
gc.set_threshold(700, 10, 10)
gc.get_threshold()
gc.set_threshold(10, 10, 10)
gc.get_threshold()
gc.set_threshold(700, 10, 10)
gc.get_threshold()
# Test gc.get_count()
gc.get_count()
# Test gc.get_stats()
gc.get_stats()
# Test gc.is_tracked()
gc.is_tracked(0)
# Test gc.garbage
gc.garbage
# Test gc.get_referrers()
gc.get_referrers(0)
# Test gc.get_referents()
gc.get_referents(0)
# Test gc.DEBUG_STATS
gc.DEBUG_STATS
# Test gc.DEBUG_COLLECTABLE
gc.DEBUG_COLLECTABLE
# Test
