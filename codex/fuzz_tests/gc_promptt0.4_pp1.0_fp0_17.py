import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()
# Test gc.get_objects()
gc.get_objects()
# Test gc.get_referrers()
gc.get_referrers()
# Test gc.get_referents()
gc.get_referents()
# Test gc.get_stats()
gc.get_stats()
# Test gc.get_threshold()
gc.get_threshold()
# Test gc.set_threshold()
gc.set_threshold()
# Test gc.is_tracked()
gc.is_tracked()
# Test gc.is_finalized()
gc.is_finalized()
# Test gc.garbage
gc.garbage
# Test gc.DEBUG_COLLECTABLE
gc.DEBUG_COLLECTABLE
# Test gc.DEBUG_UNCOLLECTABLE
gc.DEBUG_UNCOLLECTABLE
# Test gc.DEBUG_INSTANCES
gc.DEBUG_INSTANCES
# Test gc.DEBUG_OBJECTS
gc.DEBUG_OBJECTS
# Test g
