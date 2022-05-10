import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect().
gc.collect()
# Test gc.disable().
gc.disable()
gc.collect()
gc.enable()
gc.collect()
# Test gc.isenabled().
gc.isenabled()
gc.disable()
gc.isenabled()
gc.enable()
gc.isenabled()
# Test gc.get_debug().
gc.get_debug()
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
# Test gc.get_count().
gc.
