import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()
# Test gc.is_tracked()
gc.is_tracked(0)

# Test gc.garbage
gc.garbage.append(0)
gc.collect()

# Test gc.get_objects()
gc.get_objects()

# Test gc.get_referrers()
gc.get_referrers(int)

# Test gc.get_referents()
gc.get_referents(int)

# Test gc.get_stats()
gc.get_stats()

# Test gc.set_threshold()
gc.set_threshold(1)

# Test gc.enable()
gc.enable()

# Test gc.disable()
gc.disable()

# Test gc.isenabled()
gc.isenabled()

# Test gc.collect()
gc.collect()

# Test gc.call_when_freeing()
gc.call_when_freeing(lambda x: None)

# Test gc.call_when_
