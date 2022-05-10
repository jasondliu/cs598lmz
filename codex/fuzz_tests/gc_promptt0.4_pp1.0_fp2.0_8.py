import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()
gc.collect()

# Test gc.get_count()
gc.get_count()

# Test gc.get_debug()
gc.get_debug()

# Test gc.get_objects()
gc.get_objects()

# Test gc.get_referrers()
gc.get_referrers()

# Test gc.get_threshold()
gc.get_threshold()

# Test gc.set_debug()
gc.set_debug(gc.DEBUG_COLLECTABLE)
gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
gc.set_debug(gc.DEBUG_INSTANCES)
gc.set_debug(gc.DEBUG_OBJECTS)
gc.set_debug(gc.DEBUG_SAVEALL)
gc.set_debug(gc.DEBUG_LEAK)

# Test gc.set_threshold()
gc.set_threshold()
gc.set_threshold(1000)
gc.set_threshold(700, 10, 10)


