import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()

# Test gc.get_debug()
gc.get_debug()

# Test gc.set_debug()
gc.set_debug(gc.DEBUG_STATS)
gc.set_debug(gc.DEBUG_LEAK)
gc.set_debug(gc.DEBUG_COLLECTABLE)
gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
gc.set_debug(gc.DEBUG_INSTANCES)
gc.set_debug(gc.DEBUG_OBJECTS)
gc.set_debug(gc.DEBUG_SAVEALL)
gc.set_debug(gc.DEBUG_STATS | gc.DEBUG_LEAK)
gc.set_debug(gc.DEBUG_COLLECTABLE | gc.DEBUG_UNCOLLECTABLE)
gc.set_debug(gc.DEBUG_INSTANCES | gc.DEBUG_OBJECTS)
gc.set_debug(gc.DEBUG_SAVEALL | gc.DEBUG_UNCOLLECTABLE)
gc.set_debug(gc.DEBUG_LEAK | gc.DEBUG
