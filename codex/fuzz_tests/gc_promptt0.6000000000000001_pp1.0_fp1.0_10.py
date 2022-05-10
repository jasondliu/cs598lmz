import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs

a = weakref.ref(gc.collect())
a()
gc.collect()
a()
gc.collect()
del a
gc.collect()

a = weakref.ref(gc.collect())
a()
gc.collect()
a()
gc.collect()
del a
gc.collect()

a = weakref.ref(gc.collect())
a()
gc.collect()
a()
gc.collect()
del a
gc.collect()

a = weakref.ref(gc.collect())
a()
gc.collect()
a()
gc.collect()
del a
gc.collect()

a = weakref.ref(gc.collect())
a()
gc.collect()
a()
gc.collect()
del a
gc.collect()
