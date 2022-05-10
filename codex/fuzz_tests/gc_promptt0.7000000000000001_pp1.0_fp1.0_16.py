import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()

# Test gc.get_count()
gc.get_count()

# Test gc.get_threshold()
gc.get_threshold()

# Test gc.is_tracked()
gc.is_tracked(a)
gc.is_tracked(aCycle)
gc.is_tracked(b)
gc.is_tracked(bCycle)

# Test gc.set_debug()
gc.set_debug(gc.DEBUG_STATS)
gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
gc.set_debug(gc.DEBUG_SAVEALL)
gc.set_debug(gc.DEBUG_LEAK)
gc.set_debug(gc.DEBUG_STATS | gc.DEBUG_UNCOLLECTABLE)
gc.set_debug(gc.DEBUG_STATS | gc.DEBUG_UNCOLLECTABLE | gc.DEBUG_SAVEALL)
gc.set_debug(gc.DEBUG_STATS | gc.DEBUG_UNCOLLECTABLE | gc.DEBUG
