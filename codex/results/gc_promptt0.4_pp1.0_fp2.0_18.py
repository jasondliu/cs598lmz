import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()

# Test gc.garbage
gc.garbage.append(1)
gc.garbage.append(2)
gc.garbage.append(3)
gc.garbage.append(4)
gc.collect()

# Test gc.get_count
gc.get_count()

# Test gc.get_debug
gc.get_debug()

# Test gc.get_threshold
gc.get_threshold()

# Test gc.set_debug
gc.set_debug(gc.DEBUG_STATS)
gc.set_debug(gc.DEBUG_LEAK)
gc.set_debug(gc.DEBUG_COLLECTABLE)
gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
gc.set_debug(gc.DEBUG_INSTANCES)
gc.set_debug(gc.DEBUG_OBJECTS)
gc.set_debug(gc.DEBUG_SAVEALL)
gc.set_debug(gc.DEBUG_STATS | gc.DEBUG_LEAK)
gc.set_
