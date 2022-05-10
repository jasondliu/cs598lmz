import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()

# Test gc.get_referrers()
class A:
    pass
a = A()
a.x = A()
a.y = A()
a.z = A()
a.x.a = a
a.y.a = a
a.z.a = a
del a.x
del a.y
del a.z
gc.collect()

# Test gc.get_referents()
gc.get_referents(a)

# Test gc.get_objects()
gc.get_objects()

# Test gc.get_count()
gc.get_count()

# Test gc.get_threshold()
gc.get_threshold()

# Test gc.set_threshold()
gc.set_threshold(700, 10, 10)
gc.get_threshold()

# Test gc.is_tracked()
gc.is_tracked(a)

# Test gc.is_tracked()
gc.is_tracked(a)

