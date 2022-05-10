import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect
a = [object() for i in range(10) ]
del a
gc.collect()
# Test gc.disable
gc.disable()
a = [object() for i in range(10) ]
del a
gc.collect()
gc.enable()
gc.collect()
# Test gc.set_threshold
gc.set_threshold(700)
a = [object() for i in range(10) ]
del a
gc.collect()
assert gc.get_threshold() == 700
# Test gc.get_count
a = [object() for i in range(10) ]
gc.collect()
c1, c2, c3, c4 = gc.get_count()
del a
gc.collect()
assert c1 == gc.get_count()[0]
a = [object() for i in range(10) ]
gc.collect()
assert (c1+1) == gc.get_count()[0]
del a
# Test gc.get_referrers
a = [object() for i in range(10
