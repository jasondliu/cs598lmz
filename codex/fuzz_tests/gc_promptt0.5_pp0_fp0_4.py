import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    pass

f = Foo()
c = weakref.ref(f)
f2 = c()
f3 = c()
del f, f2, f3
gc.collect()
# Test gc.get_debug()

gc.set_debug(gc.DEBUG_STATS)
gc.get_debug()
gc.set_debug(gc.DEBUG_COLLECTABLE)
gc.get_debug()
gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
gc.get_debug()
gc.set_debug(gc.DEBUG_INSTANCES)
gc.get_debug()
gc.set_debug(gc.DEBUG_OBJECTS)
gc.get_debug()
gc.set_debug(gc.DEBUG_SAVEALL)
gc.get_debug()
gc.set_debug(gc.DEBUG_LEAK)
gc.get_debug()
# Test gc.get_threshold()

gc.get_threshold()
# Test gc.set_threshold()

gc.set_threshold
