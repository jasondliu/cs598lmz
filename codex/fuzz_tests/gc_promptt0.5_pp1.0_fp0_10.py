import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class A:
    pass
a = A()
a = None
gc.collect()
gc.collect()
gc.collect()
gc.collect()
# Test gc.get_objects()
class A:
    pass
a = A()
a = None
gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.get_objects()
# Test gc.get_referrers()
class A:
    pass
a = A()
a = None
gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.get_referrers(A)
# Test gc.get_referents()
class A:
    pass
a = A()
a = None
gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.get_referents(A)
# Test gc.get_stats()
class A:
    pass
a = A()
a = None
gc.collect()
gc.collect()
gc.collect()
gc.collect()

