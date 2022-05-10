import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class A:
    pass
a = A()
a.b = A()
a.b.a = a
del a
gc.collect()
# Test gc.garbage
class A:
    pass
a = A()
a.b = A()
a.b.a = a
del a
gc.garbage[0].b = None
gc.collect()
# Test gc.get_objects()
class A:
    pass
a = A()
a.b = A()
a.b.a = a
del a
gc.collect()
# Test gc.get_referrers()
class A:
    pass
a = A()
a.b = A()
a.b.a = a
del a
gc.collect()
# Test gc.get_referents()
class A:
    pass
a = A()
a.b = A()
a.b.a = a
del a
gc.collect()
# Test gc.is_tracked()
class A:
    pass
a = A()
a.
