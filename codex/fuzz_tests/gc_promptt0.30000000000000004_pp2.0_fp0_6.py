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
class A:
    pass

a = A()
b = A()
a.b = b
b.a = a
del a
del b
gc.collect()
# Test gc.get_referrers()
class A:
    pass

a = A()
b = A()
a.b = b
b.a = a
del a
del b
gc.collect()
# Test gc.get_referents()
class A:
    pass

a = A()
b = A()
a.b = b
b.a = a
del a
del b
gc.collect()
# Test gc.get_threshold()
gc.get_threshold()
# Test gc.set_threshold()
gc.set_threshold(1, 2, 3)
gc.get_threshold()
# Test g
