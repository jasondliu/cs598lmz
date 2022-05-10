import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()
gc.collect()
gc.collect()

# Test gc.get_objects()
gc.get_objects()

# Test gc.get_referrers()
gc.get_referrers(gc)

# Test gc.get_referents()
gc.get_referents(gc)

# Test gc.is_tracked()
gc.is_tracked(gc)
gc.is_tracked(gc.get_objects)
gc.is_tracked(gc.get_referrers)
gc.is_tracked(gc.get_referents)
gc.is_tracked(gc.is_tracked)
gc.is_tracked(gc.get_threshold)
gc.is_tracked(gc.get_count)
gc.is_tracked(gc.set_threshold)
gc.is_tracked(gc.enable)
gc.is_tracked(gc.disable)
gc.is_tracked(gc.isenabled)
gc.is_tracked(gc
