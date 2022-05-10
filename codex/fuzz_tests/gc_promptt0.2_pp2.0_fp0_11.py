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
gc.collect()
print gc.garbage
# Test gc.get_objects()
class A:
    pass
a = A()
a.b = A()
a.b.a = a
del a
gc.collect()
print len(gc.get_objects())
# Test gc.get_referrers()
class A:
    pass
a = A()
a.b = A()
a.b.a = a
del a
gc.collect()
print len(gc.get_referrers(gc.garbage[0]))
# Test gc.get_referents()
class A:
    pass
a = A()
a.b = A()
a.b.a = a
del a
gc.collect()
