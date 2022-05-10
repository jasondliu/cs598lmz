import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() doesn't crash
gc.collect()
gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
gc.enable()
gc.set_threshold(100, 10, 1)
gc.disable()
gc.isenabled()
gc.debug
