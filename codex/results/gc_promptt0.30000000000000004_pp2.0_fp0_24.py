import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class A:
    pass
a = A()
a.a = A()
a.a.a = a
del a
gc.collect()
# Test gc.get_objects()
gc.get_objects()
# Test gc.get_referrers()
gc.get_referrers(A)
# Test gc.get_referents()
gc.get_referents(A)
# Test gc.is_tracked()
gc.is_tracked(A)
# Test gc.is_tracked()
gc.is_tracked(A())
# Test gc.get_count()
gc.get_count()
# Test gc.get_stats()
gc.get_stats()
# Test gc.garbage
gc.garbage
# Test gc.get_threshold()
gc.get_threshold()
# Test gc.set_threshold()
gc.set_threshold(700, 10, 10)
# Test gc.get_threshold()
gc.get_threshold()
# Test g
