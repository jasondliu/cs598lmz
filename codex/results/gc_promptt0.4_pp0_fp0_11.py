import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class A:
    pass

a = A()
del a
gc.collect()
# Test gc.get_referrers()
class A:
    pass

a = A()
del a
gc.collect()
gc.get_referrers(A)
# Test gc.get_referents()
class A:
    pass

a = A()
del a
gc.collect()
gc.get_referents(A)
# Test gc.get_objects()
class A:
    pass

a = A()
del a
gc.collect()
gc.get_objects()
# Test gc.is_tracked()
class A:
    pass

a = A()
del a
gc.collect()
gc.is_tracked(A)
# Test gc.set_threshold()
class A:
    pass

a = A()
del a
gc.collect()
gc.set_threshold(1,1,1)
gc.get_threshold()
# Test gc.get_threshold()
