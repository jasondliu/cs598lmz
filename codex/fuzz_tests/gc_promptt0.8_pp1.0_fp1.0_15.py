import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() call.
gc.collect()

def x():
    l = []
    for i in range(10):
        l.append(weakref.ref(l))
        l.append(weakref.ref(l))
    return l

o = x()
del o
gc.collect()

gc.set_debug(gc.DEBUG_UNCOLLECTABLE | gc.DEBUG_COLLECTABLE)
gc.collect()

# Check the simplification of gc.DEBUG_* flags.
gc.set_debug(0)
gc.set_debug(gc.DEBUG_COLLECTABLE | gc.DEBUG_COLLECTABLE)
gc.set_debug(gc.DEBUG_UNCOLLECTABLE | gc.DEBUG_UNCOLLECTABLE)
gc.set_debug(1)
gc.set_debug(gc.DEBUG_COLLECTABLE)
gc.set_debug(gc.DEBUG_UNCOLLECTABLE)

# Test gc.get_referrers().
# Create some objects.
a, b, c, d, e, f, g = 'abcdefg
