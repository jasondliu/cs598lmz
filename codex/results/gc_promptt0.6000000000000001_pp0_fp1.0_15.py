import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
# Collect all objects (including referenced objects)
gc.collect()

# Test gc.get_debug()
gc.get_debug()

# Test gc.get_threshold()
gc.get_threshold()

# Test gc.set_debug()
gc.set_debug(gc.DEBUG_COLLECTABLE)

# Test gc.set_threshold()
gc.set_threshold(700, 10, 10)
gc.get_threshold()
gc.set_threshold(10, 700, 10)
gc.get_threshold()
gc.set_threshold(10, 10, 700)
gc.get_threshold()

# Test gc.get_count()
gc.get_count()

# Test gc.set_threshold()
gc.set_threshold(700, 10, 10)
gc.get_count()
gc.set_threshold(10, 700, 10)
gc.get_count()
gc.set_threshold(10, 10, 700)
gc.get_count()

# Test
