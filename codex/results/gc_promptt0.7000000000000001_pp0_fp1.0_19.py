import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect
gc.collect()
gc.collect()

# Test gc.get_threshold
gc.get_threshold()

# Test gc.get_count
gc.get_count()

# Test gc.set_threshold
gc.set_threshold(2)
gc.set_threshold(3)
gc.set_threshold(1)

# Test gc.enable
gc.enable()
gc.disable()

# Test gc.isenabled
gc.isenabled()

# Test gc.set_debug
gc.set_debug(gc.DEBUG_STATS)
gc.set_debug(gc.DEBUG_COLLECTABLE)
gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
gc.set_debug(gc.DEBUG_INSTANCES)
gc.set_debug(gc.DEBUG_OBJECTS)
gc.set_debug(gc.DEBUG_SAVEALL)
gc.set_debug(gc.DEBUG_LEAK)

# Test gc.get_objects
objects = gc.get_objects()
