import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect - this should immediately collect this object.
w = weakref.ref(C())
gc.collect()

# Test gc.garbage - this should never collect this object.
w = C()
gc.garbage.append(w)
gc.collect()
print(gc.garbage)
