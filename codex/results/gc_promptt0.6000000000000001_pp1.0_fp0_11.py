import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class C(object):
    pass

o = C()

print gc.collect()

# Test gc.get_threshold()

# Test gc.set_threshold()

# Test gc.get_count()

gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
# Test gc.get_objects()

# Test gc.get_referrers()

# Test gc.get_referents()

# Test gc.is_tracked()

# Test gc.is_finalized()

# Test gc.garbage

# Test gc.DEBUG_STATS

# Test gc.DEBUG_COLLECTABLE

# Test gc.DEBUG_UNCOLLECTABLE

# Test gc.DEBUG_INSTANCES

# Test gc.DEBUG_OBJECTS

# Test gc.DEBUG_SAVEALL

# Test gc.DEBUG_LEAK

# Test gc.callbacks
