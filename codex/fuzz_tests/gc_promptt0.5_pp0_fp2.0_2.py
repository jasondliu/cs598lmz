import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect_generations
gc.collect_generations()
gc.collect_generations()

# Test gc.get_threshold
gc.get_threshold()

# Test gc.set_threshold
gc.set_threshold()
gc.set_threshold(2)
gc.set_threshold(2, 2, 2)

# Test gc.get_count
gc.get_count()

# Test gc.enable
gc.enable()

# Test gc.disable
gc.disable()

# Test gc.isenabled
gc.isenabled()

# Test gc.collect
gc.collect()

# Test gc.set_debug
gc.set_debug(gc.DEBUG_STATS)
gc.set_debug(gc.DEBUG_STATS | gc.DEBUG_LEAK)
gc.set_debug(gc.DEBUG_STATS | gc.DEBUG_LEAK)
gc.set_debug(gc.DEBUG_STATS | gc.DEBUG_LEAK | gc.DEBUG_COLLECTABLE)
gc.set
