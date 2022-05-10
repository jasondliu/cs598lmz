import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()

# Test gc.get_debug()
gc.get_debug()

# Test gc.get_threshold()
gc.get_threshold()

# Test gc.set_debug()
gc.set_debug(gc.DEBUG_STATS)
gc.set_debug(gc.DEBUG_LEAK)
gc.set_debug(0)

# Test gc.set_threshold()
gc.set_threshold(700, 10, 10)
gc.set_threshold(10)

# Test gc.get_count()
gc.get_count()

# Test gc.get_stats()
gc.get_stats()

# Test gc.garbage
gc.garbage

# Test gc.isenabled()
gc.isenabled()

# Test gc.enable()
gc.enable()

# Test gc.disable()
gc.disable()

# Test gc.isdisabled()
gc.isdisabled()

# Test gc.collect()
gc.collect()

#
