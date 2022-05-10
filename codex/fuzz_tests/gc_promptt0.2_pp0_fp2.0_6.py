import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()
# Test gc.get_objects()
gc.get_objects()
# Test gc.get_referrers()
gc.get_referrers(gc)
# Test gc.get_referents()
gc.get_referents(gc)
# Test gc.get_threshold()
gc.get_threshold()
# Test gc.set_threshold()
gc.set_threshold(1, 2, 3)
# Test gc.get_count()
gc.get_count()
# Test gc.set_debug()
gc.set_debug(gc.DEBUG_COLLECTABLE | gc.DEBUG_UNCOLLECTABLE | gc.DEBUG_INSTANCES | gc.DEBUG_OBJECTS)
# Test gc.is_tracked()
gc.is_tracked(gc)
# Test gc.garbage
gc.garbage
# Test gc.callbacks
gc.callbacks
# Test gc.DEBUG_STATS
gc.DEBUG_STATS
# Test gc.DEBUG
