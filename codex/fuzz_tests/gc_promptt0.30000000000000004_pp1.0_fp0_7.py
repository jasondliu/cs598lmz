import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class A:
    pass

a = A()
b = A()
a.b = b
b.a = a
del a, b
gc.collect()
# Test gc.garbage
class A:
    pass

a = A()
b = A()
a.b = b
b.a = a
del a, b
gc.collect()
gc.garbage
# Test gc.get_count()
gc.get_count()
# Test gc.get_debug()
gc.get_debug()
# Test gc.get_objects()
gc.get_objects()
# Test gc.get_referrers()
gc.get_referrers(int)
# Test gc.get_threshold()
gc.get_threshold()
# Test gc.set_debug()
gc.set_debug(gc.DEBUG_STATS)
gc.set_debug(gc.DEBUG_LEAK)
gc.set_debug(gc.DEBUG_COLLECTABLE)
gc.set_debug(gc.DEBUG_UNCOLLECTABLE
