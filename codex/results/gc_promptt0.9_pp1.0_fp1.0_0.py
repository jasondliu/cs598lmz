import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref pointing to a tuple.
# This was a bug in Python.

wref = weakref.ref(tuple())
gc.collect()

print wref() is None
