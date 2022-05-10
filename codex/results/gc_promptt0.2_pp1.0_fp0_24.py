import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class A:
    pass

a = A()
b = A()
a.b = b
b.a = a
del a
del b
gc.collect()

# Test gc.get_objects()
gc.get_objects()

# Test gc.get_referrers()
gc.get_referrers(A)

# Test gc.get_referents()
gc.get_referents(A)

# Test gc.is_tracked()
gc.is_tracked(A)

# Test gc.get_threshold()
gc.get_threshold()

# Test gc.set_threshold()
gc.set_threshold(700, 10, 10)
gc.get_threshold()

# Test gc.get_count()
gc.get_count()

# Test gc.garbage
gc.garbage

# Test gc.set_debug()
gc.set_debug(gc.DEBUG_STATS)
gc.set_debug(gc.DEBUG_LEAK)
