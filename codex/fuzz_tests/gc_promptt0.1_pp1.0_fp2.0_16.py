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
# Test gc.get_referrers()
class A:
    pass

a = A()
a.b = A()
a.b.a = a

gc.get_referrers(a)
gc.get_referrers(a.b)
gc.get_referrers(a.b.a)
# Test gc.get_referents()
class A:
    pass

a = A()
a.b = A()
a.b.a = a

gc.get_referents(a)
gc.get_referents(a.b)
gc.get_referents(a.b.a)
# Test gc.get_objects()
class A:
    pass

a = A()
a.b = A()
a.b.a = a

gc.get_objects()
# Test gc.get_stats()
gc
