import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()
# Test gc.get_objects()
gc.get_objects()
# Test gc.get_referrers()
gc.get_referrers(gc.get_objects())
# Test gc.get_referents()
gc.get_referents(gc.get_objects())
# Test gc.get_threshold()
gc.get_threshold()
# Test gc.set_threshold()
gc.set_threshold(100, 10, 10)
# Test gc.get_count()
gc.get_count()
# Test gc.set_debug()
gc.set_debug(gc.DEBUG_STATS)
# Test gc.is_tracked()
gc.is_tracked(gc.get_objects())
# Test gc.is_finalized()
gc.is_finalized(gc.get_objects())
# Test gc.garbage
gc.garbage
# Test gc.callbacks
gc.callbacks
# Test gc.disable()
gc.disable()
# Test g
