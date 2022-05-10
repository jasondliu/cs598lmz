import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() after creating a weakref cycle

def f():
    l = []
    l.append(l)
    return weakref.ref(l)

r = f()
r()
gc.collect()
print "collectable:", gc.collect()
print "unreachable:", gc.collect(0)
