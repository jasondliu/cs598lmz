import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() limit keyword.
gc.collect(1,2)
gc.collect(1)
gc.collect(generation=1)
try:
    gc.collect(1, 1)
except TypeError:
    pass
else:
    raise RuntimeError, "no TypeError raised"

# Test gc.get_debug().
gc.get_debug()

# Test gc.get_objects().
x = gc.get_objects()
x = x[:10]
id(x[0])

# Test gc.get_threshold().
gc.get_threshold()

# Test gc.set_debug().
gc.set_debug(gc.DEBUG_LEAK)
gc.set_debug(gc.DEBUG_STATS)
gc.set_debug(gc.DEBUG_COLLECTABLE)

# Test gc.set_threshold().
gc.set_threshold(700, 10, 10)
gc.set_threshold(700, 10)
gc.set_threshold(700)

# Test weakref.getweakrefcount() and
