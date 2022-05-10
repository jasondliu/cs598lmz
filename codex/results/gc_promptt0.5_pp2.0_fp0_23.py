import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()

# Test gc.get_threshold()
gc.get_threshold()

# Test gc.set_threshold()
gc.set_threshold(100, 10, 10)
gc.get_threshold()
gc.set_threshold(0, 0, 0)
gc.get_threshold()

# Test gc.get_count()
gc.get_count()

# Test gc.set_debug()
gc.set_debug(gc.DEBUG_COLLECTABLE)
gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
gc.set_debug(gc.DEBUG_INSTANCES)
gc.set_debug(gc.DEBUG_OBJECTS)
gc.set_debug(gc.DEBUG_SAVEALL)
gc.set_debug(gc.DEBUG_LEAK)

# Test gc.get_debug()
gc.get_debug()

# Test gc.garbage()
gc.garbage

# Test gc.enable()
gc.enable()

# Test gc
