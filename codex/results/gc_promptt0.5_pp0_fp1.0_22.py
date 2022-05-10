import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()

# Test gc.set_threshold()
gc.set_threshold(2, 3, 4)
gc.collect()
gc.set_threshold(3, 4, 5)
gc.collect()

# Test gc.get_threshold()
assert gc.get_threshold() == (3, 4, 5)

# Test gc.get_count()
assert gc.get_count() == (0, 0, 0)

# Test gc.get_stats()
assert gc.get_stats() == (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
