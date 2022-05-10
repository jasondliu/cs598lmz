import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()

# Test gc.get_referrers()
gc.get_referrers(object())

# Test gc.get_referents()
gc.get_referents(object())

# Test gc.get_objects()
gc.get_objects()

# Test gc.get_count()
gc.get_count()

# Test gc.get_stats()
gc.get_stats()

# Test gc.is_tracked()
gc.is_tracked(object())

# Test gc.set_threshold()
gc.set_threshold(1, 2, 3)

# Test gc.enable()
gc.enable()

# Test gc.disable()
gc.disable()

# Test gc.isenabled()
gc.isenabled()

# Test gc.collect()
gc.collect()

# Test gc.garbage
gc.garbage

# Test gc.set_debug()
gc.set_debug(gc.DEBUG_STATS)


