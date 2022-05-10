import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()

# Test gc.get_count()
gc.get_count()

# Test gc.get_stats()
gc.get_stats()

# Test gc.get_threshold()
gc.get_threshold()

# Test gc.set_threshold()
gc.set_threshold(700, 10, 10)
gc.get_threshold()

# Test gc.enable()
gc.enable()

# Test gc.disable()
gc.disable()

# Test gc.isenabled()
gc.isenabled()

# Test gc.collect()
gc.collect()

# Test gc.set_debug()
gc.set_debug(gc.DEBUG_STATS)
gc.set_debug(gc.DEBUG_LEAK)
gc.set_debug(0)

# Test gc.get_objects()
gc.get_objects()

# Test gc.get_referrers()
gc.get_referrers(gc)

# Test gc.get_referent
