import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()

# Test gc.get_objects()
gc.get_objects()

# Test gc.get_referrers()
gc.get_referrers(None)

# Test gc.get_referents()
gc.get_referents(None)

# Test gc.is_tracked()
gc.is_tracked(None)

# Test gc.garbage
gc.garbage

# Test gc.disable()
gc.disable()
gc.collect()
gc.enable()

# Test gc.isenabled()
gc.isenabled()

# Test gc.set_debug()
gc.set_debug(gc.DEBUG_LEAK)
gc.set_debug(gc.DEBUG_COLLECTABLE)

# Test gc.set_threshold()
gc.set_threshold(0)
gc.set_threshold(1)
gc.set_threshold(2)
gc.set_threshold(3)

# Test gc.get_count()
gc.get
