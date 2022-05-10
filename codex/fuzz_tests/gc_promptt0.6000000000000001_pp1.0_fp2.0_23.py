import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()

class C:
    pass

c = C()
del c

print(gc.collect())
print(gc.collect())
print(gc.collect())
# Test gc.get_count()
print(gc.get_count())
print(gc.get_count())
# Test gc.get_threshold()
print(gc.get_threshold())
# Test gc.set_threshold()
gc.set_threshold(1,1,1)
# Test gc.is_tracked()
print(gc.is_tracked(1))
# Test gc.set_debug()
gc.set_debug(gc.DEBUG_STATS)
gc.set_debug(gc.DEBUG_LEAK)
gc.set_debug(gc.DEBUG_COLLECTABLE)
gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
gc.set_debug(gc.DEBUG_INSTANCES)
gc.set_debug(gc.DEBUG_OBJECTS)
gc.set_debug(0)
gc.set
