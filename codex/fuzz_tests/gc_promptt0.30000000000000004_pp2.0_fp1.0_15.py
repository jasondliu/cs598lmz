import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()
# Test gc.get_count()
gc.get_count()
# Test gc.get_debug()
gc.get_debug()
# Test gc.get_threshold()
gc.get_threshold()
# Test gc.set_debug()
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.set_threshold()
gc.set_threshold(700, 10, 10)
# Test gc.get_objects()
len(gc.get_objects())
# Test gc.get_referrers()
len(gc.get_referrers(gc))
# Test gc.get_referents()
len(gc.get_referents(gc))
# Test gc.is_tracked()
gc.is_tracked(gc)
# Test gc.is_finalized()
gc.is_finalized(gc)
# Test gc.garbage
gc.garbage
# Test gc.DEBUG_STATS
gc.DEBUG_STATS
# Test gc
