import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()
# Test gc.get_referrers()
gc.get_referrers(gc)
# Test gc.get_referents()
gc.get_referents(gc)
# Test gc.get_objects()
gc.get_objects()
# Test gc.get_stats()
gc.get_stats()
# Test gc.get_threshold()
gc.get_threshold()
# Test gc.set_threshold()
gc.set_threshold(1, 1, 1)
# Test gc.is_tracked()
gc.is_tracked(gc)
# Test gc.is_finalized()
gc.is_finalized(gc)
# Test gc.garbage
gc.garbage
# Test gc.DEBUG_STATS
gc.DEBUG_STATS
# Test gc.DEBUG_LEAK
gc.DEBUG_LEAK
# Test gc.DEBUG_COLLECTABLE
gc.DEBUG_COLLECTABLE
# Test gc.DEBUG_UNCOLLECTABLE
gc.DEBUG_
