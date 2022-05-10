import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs.

class A:
    pass

a = A()
a.x = weakref.ref(a)
gc.collect()
print 'ok'
