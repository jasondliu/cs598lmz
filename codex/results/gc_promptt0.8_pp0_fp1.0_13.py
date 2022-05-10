import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs
class C:
    pass
c = C()
w = weakref.ref(c)
gc.collect()
# Test gc.collect() with weakrefs with callbacks
class C2:
    pass
def callback(r):
    pass
c2 = C2()
w2 = weakref.ref(c2, callback)
gc.collect()
