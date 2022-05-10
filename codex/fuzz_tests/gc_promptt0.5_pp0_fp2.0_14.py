import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class A(object):
    pass

a = A()
a.b = A()
a.b.c = a
del a
gc.collect()
# Test gc.garbage
class A(object):
    pass

a = A()
a.b = A()
a.b.c = a
del a

class B(object):
    pass

b = B()
b.a = A()
b.a.b = b
del b

gc.collect()
print(gc.garbage)
# Test gc.get_debug()
gc.set_debug(gc.DEBUG_COLLECTABLE)
gc.get_debug()
# Test gc.get_objects()
gc.get_objects()
# Test gc.get_referrers()
gc.get_referrers(None)
# Test gc.get_threshold()
gc.get_threshold()
# Test gc.is_tracked()
gc.is_tracked(None)
# Test gc.set_debug()
gc.set_
