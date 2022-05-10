import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()

# Test gc.get_referrers()
class A:
    pass

a = A()
ref = weakref.ref(a)
gc.get_referrers(a)

# Test gc.get_referents()
gc.get_referents(a)

# Test gc.get_objects()
gc.get_objects()

# Test gc.get_stats()
gc.get_stats()

# Test gc.is_tracked()
gc.is_tracked(a)

# Test gc.set_debug()
gc.set_debug(gc.DEBUG_STATS)
gc.set_debug(gc.DEBUG_LEAK)
gc.set_debug(gc.DEBUG_COLLECTABLE)
gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
gc.set_debug(0)

# Test gc.get_count()
gc.get_count()

# Test gc.get_threshold()
gc.get_threshold()

#
