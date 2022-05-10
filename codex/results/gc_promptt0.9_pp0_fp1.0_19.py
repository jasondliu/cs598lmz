import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with an unfreed weak reference
# to a cyclical list.
l = [1,2,3]
a = weakref.ref(l)
l.append(l)
gc.collect()
del l
print gc.collect()
# Now free a.
del a
gc.collect()
print gc.collect()

# Test with and without gc enabled.
gc.disable()
l = [1,2,3]
a = weakref.ref(l)
l.append(l)
gc.collect()
del l
print gc.collect()
# Now free a.
del a
gc.collect()
print gc.collect()
gc.enable()
# Still no collection
l = [1,2,3]
a = weakref.ref(l)
l.append(l)
gc.collect()
del l
print gc.collect()
# Now free a.
del a
gc.collect()
print gc.collect()
