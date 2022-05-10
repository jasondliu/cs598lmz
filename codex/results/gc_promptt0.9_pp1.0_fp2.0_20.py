import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collectable()
gc.collectable()

# Test gc.get_threshold()
gc.get_threshold()

gc.collect()

# Test gc.set_threshold()
gc.set_threshold(1 << 16)
gc.set_threshold(1 << 16, 1 << 16, 1 << 16)
# Test gc.get_debug()
gc.get_debug()

gc.collect()

# Test gc.set_debug()
gc.set_debug(0)
gc.set_debug(gc.DEBUG_STATS)
gc.set_debug(gc.DEBUG_LEAK)
gc.set_debug(gc.DEBUG_STATS | gc.DEBUG_LEAK)
gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
gc.set_debug(gc.DEBUG_STATS | gc.DEBUG_UNCOLLECTABLE)
# Test gc.is_tracked()
gc.is_tracked(object())

gc.collect()

# Test gc.get_objects()
gc.get_objects
