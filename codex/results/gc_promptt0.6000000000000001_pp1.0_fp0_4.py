import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect
class A:
    pass
a = A()
a.x = a
a.y = a
a.z = a
del a
gc.collect()
# Test weakref
class A:
    pass
a = A()
a.x = a
a.y = a
a.z = a
del a
gc.collect()
# Test gc.get_referrers
gc.get_referrers()
# Test gc.get_referents
gc.get_referents()
# Test gc.get_objects
gc.get_objects()
# Test gc.get_stats
gc.get_stats()
# Test gc.get_threshold
gc.get_threshold()
# Test gc.set_threshold
gc.set_threshold()
# Test gc.DEBUG_STATS
gc.DEBUG_STATS
gc.get_stats()
# Test gc.DEBUG_LEAK
gc.DEBUG_LEAK
gc.get_stats()
# Test gc.DEBUG_SAVEALL
gc.DEBUG_SAVE
