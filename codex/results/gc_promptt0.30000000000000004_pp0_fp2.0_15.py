import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with uncollectable objects

class C:
    pass

def f():
    c = C()
    c.x = weakref.ref(c)

f()
gc.collect()
gc.collect()

# The following should print "gc: collectable <C instance at ..."

gc.collect()
gc.collect()
