import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() will find it
c = weakref.ref(C())
del c
gc.collect()
# Test gc.collect() won't find it
c = C()
c.__weakref__ = weakref.ref(C())
c.__weakref__ = None
c = weakref.ref(c)
del c
gc.collect()
# Test gc.collect() won't find it
c = C()
c.__weakref__ = C()
c.__weakref__ = None
c = weakref.ref(c)
del c
gc.collect()
