import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect with weakref
gc.collect()
x = list(range(20))
d = [weakref.ref(x) for x in range(20)]
gc.collect()
del x
gc.collect()
