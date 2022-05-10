import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class A:
    pass
a = A()
a.b = A()
a.b.c = a
del a
gc.collect()
# Test gc.get_referrers()
class A:
    pass
a = A()
a.b = A()
a.b.c = a
a.b.c.d = a.b
a.b.c.d.e = a.b.c
del a
gc.collect()
# Test gc.get_referents()
class A:
    pass
a = A()
a.b = A()
a.b.c = a
a.b.c.d = a.b
a.b.c.d.e = a.b.c
del a
gc.collect()
# Test gc.get_objects()
class A:
    pass
a = A()
a.b = A()
a.b.c = a
a.b.c.d = a.b
a.b.c.d.e = a.b.c
del a

