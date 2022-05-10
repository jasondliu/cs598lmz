import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()
gc.garbage

# Test gc.get_debug()
gc.get_debug()
gc.set_debug(0)
gc.get_debug()
gc.set_debug(gc.DEBUG_COLLECTABLE)
gc.get_debug()

# Test gc.get_threshold()
gc.get_threshold()

# Test gc.is_tracked() and gc.is_tracked()
gc.is_tracked(1)
gc.is_tracked(1.1)
gc.is_tracked('foo')
gc.is_tracked(gc)

# Test gc.set_debug()
gc.set_debug(gc.DEBUG_STATS)
gc.get_debug()
gc.set_debug(gc.DEBUG_LEAK)
gc.get_debug()
gc.set_debug(0)
gc.get_debug()

# Test gc.set_threshold()
gc.set_threshold(1, 1, 1)
gc.set_threshold(0)
