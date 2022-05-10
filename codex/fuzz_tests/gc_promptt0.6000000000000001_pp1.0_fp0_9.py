import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()

# Test if gc.DEBUG_STATS works
gc.set_debug(gc.DEBUG_STATS)
gc.collect()
gc.set_debug(0)

# Test if gc.DEBUG_LEAK works
gc.set_debug(gc.DEBUG_LEAK)
gc.collect()
gc.set_debug(0)

# Test gc.get_debug()
gc.get_debug()

# Test gc.get_stats()
gc.get_stats()

# Test gc.is_tracked()
gc.is_tracked(gc)

# Test gc.get_threshold()
gc.get_threshold()

# Test gc.set_threshold()
gc.set_threshold(1, 2, 3)
gc.get_threshold()
gc.set_threshold(700, 10, 10)
gc.get_threshold()

# Test gc.get_objects()
len(gc.get_objects())

# Test gc.get_referrers()
