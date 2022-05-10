import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()
# Test gc.is_tracked()
gc.is_tracked(obj)
# Test gc.get_referrers()
gc.get_referrers(obj)
# Test gc.get_referents()
gc.get_referents(obj)
# Test gc.get_objects()
gc.get_objects()
# Test gc.get_stats()
gc.get_stats()
# Test gc.garbage
gc.garbage
# Test gc.set_threshold()
gc.set_threshold(700, 10, 10)
# Test gc.get_threshold()
gc.get_threshold()
# Test gc.enable()
gc.enable()
# Test gc.disable()
gc.disable()
# Test gc.isenabled()
gc.isenabled()
# Test gc.callbacks
gc.callbacks
# Test gc.collect()
gc.collect()
# Test gc.collect()
gc.collect()
# Test gc.collect()
gc.
