import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()

class A:
    pass

a = A()
del a
gc.collect()

# Test gc.set_threshold()
gc.set_threshold(1, 2, 3)
gc.collect()

# Test gc.get_threshold()
gc.get_threshold()

# Test gc.get_count()
gc.get_count()

# Test gc.get_stats()
gc.get_stats()

# Test gc.garbage
gc.garbage

# Test gc.disable()
gc.disable()
gc.collect()

# Test gc.enable()
gc.enable()
gc.collect()

# Test gc.isenabled()
gc.isenabled()

# Test gc.set_debug()
gc.set_debug(gc.DEBUG_STATS)
gc.set_debug(gc.DEBUG_COLLECTABLE)
gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
gc.set_debug(gc.DEBUG_INSTANCES)

