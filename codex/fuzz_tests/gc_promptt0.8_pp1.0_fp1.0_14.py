import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()
1
# Test implicit gc.collect()
gc.garbage.append((gc.garbage, ))
1
# Test gc.garbage
gc.collect()
gc.garbage

gc.garbage = []

# Test gc.get_threshold()
gc.get_threshold()
gc.set_threshold(70, 10, 5)
gc.get_threshold()

# Test gc.get_count()
gc.set_threshold(700)
gc.get_count()

# Test gc.set_debug()
gc.set_debug(gc.DEBUG_STATS)
gc.set_debug(gc.DEBUG_COLLECTABLE | gc.DEBUG_UNCOLLECTABLE)
gc.set_debug(0)

# Test gc.get_objects()
len(gc.get_objects())

# Test gc.is_tracked()
gc.is_tracked(gc)

# Test gc.get_referrers()
a = []
len(gc.get_re
