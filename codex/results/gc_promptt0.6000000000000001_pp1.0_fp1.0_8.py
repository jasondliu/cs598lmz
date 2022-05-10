import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect().  This is a very weak test since it is timing
# dependent.  It is here mostly to ensure that the method is
# present and that it runs without a fatal error.
class A:
    pass

for i in range(10):
    a = A()
    a = None

gc.collect()
# Test gc.disable() and gc.isenabled().
gc.disable()
gc.collect()
gc.isenabled()
gc.enable()
gc.collect()
gc.isenabled()
# Test gc.get_debug().
gc.get_debug()
gc.set_debug(gc.DEBUG_LEAK)
gc.get_debug()
gc.set_debug(gc.DEBUG_STATS)
gc.get_debug()
gc.set_debug(gc.DEBUG_COLLECTABLE)
gc.get_debug()
gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
gc.get_debug()
gc.set_debug(gc.DEBUG_INSTANCES)
gc.get_debug()
gc.set_debug(gc.DEBUG
