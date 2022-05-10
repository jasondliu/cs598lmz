import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class A(object):
    pass

a = A()
a.b = A()
a.b.a = a
del a
gc.collect()
# Test gc.get_referrers()
class A(object):
    pass

a = A()
a.b = A()
a.b.a = a
del a
gc.collect()
# Test gc.get_referents()
class A(object):
    pass

a = A()
a.b = A()
a.b.a = a
del a
gc.collect()
# Test gc.get_objects()
class A(object):
    pass

a = A()
a.b = A()
a.b.a = a
del a
gc.collect()
# Test gc.get_count()
class A(object):
    pass

a = A()
a.b = A()
a.b.a = a
del a
gc.collect()
# Test gc.get_stats()
class A(object):
    pass

