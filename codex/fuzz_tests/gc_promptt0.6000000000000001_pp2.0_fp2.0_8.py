import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()
gc.collect()

# Test gc.garbage
class Foo:
    pass
f = Foo()
f.x = f
gc.garbage.append(f)
gc.collect()
del f
gc.collect()

# Test gc.get_count
gc.get_count()

# Test gc.get_debug
gc.get_debug()

# Test gc.set_debug
gc.set_debug(0)
gc.set_debug(gc.DEBUG_STATS)
gc.set_debug(gc.DEBUG_COLLECTABLE)
gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
gc.set_debug(gc.DEBUG_INSTANCES)
gc.set_debug(gc.DEBUG_OBJECTS)
gc.set_debug(gc.DEBUG_SAVEALL)
gc.set_debug(gc.DEBUG_LEAK)
gc.set_debug(gc.DEBUG_STATS | gc.DEBUG_COLLECTABLE | gc.DEBUG_UNCOLLECTABLE)

#
