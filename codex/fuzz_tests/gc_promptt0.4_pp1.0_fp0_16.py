import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() without any uncollectable objects around.
gc.collect()
gc.collect()
gc.collect()
# Test gc.collect() with a single uncollectable object.
def callback(ignored):
    print "Callback called"
ob = weakref.ref(object(), callback)
gc.collect()
gc.collect()
gc.collect()
# Test gc.collect() with two uncollectable objects, one of which has a callback.
ob2 = weakref.ref(object())
gc.collect()
gc.collect()
gc.collect()
# Test gc.collect() with a cycle.
ob3 = object()
ob4 = object()
ob3.ref = ob4
ob4.ref = ob3
del ob3, ob4
gc.collect()
gc.collect()
gc.collect()
print "Done."
