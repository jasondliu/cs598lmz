import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() after registering an object as collectable.
# Test that gc.collect() returns the right value.

gc.collect()
l = []
l.append(l)
wr = weakref.ref(l)
id_l = id(l)
gc.collect()
print gc.collect() == 0

gc.collect()
del l
print gc.collect() == 1

print wr() is None
del wr
print gc.collect() == 0
