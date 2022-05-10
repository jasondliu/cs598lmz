import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()
# Test gc.get_referrers()
gc.get_referrers(None)
# Test gc.get_referents()
gc.get_referents(None)
# Test gc.get_objects()
gc.get_objects()
# Test gc.get_stats()
gc.get_stats()
# Test gc.get_threshold()
gc.get_threshold()
# Test gc.set_threshold()
gc.set_threshold(0, 0, 0)
# Test gc.is_tracked()
gc.is_tracked(None)
# Test gc.garbage
gc.garbage
# Test gc.set_debug()
gc.set_debug(0)
# Test gc.callbacks
gc.callbacks
# Test gc.disable()
gc.disable()
# Test gc.enable()
gc.enable()
# Test gc.isenabled()
gc.isenabled()
# Test gc.collect()
gc.collect()
# Test gc
