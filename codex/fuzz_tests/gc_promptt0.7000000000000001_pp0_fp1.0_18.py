import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()
gc.collect()
gc.collect()

# Test weakref
x = weakref.ref(5)
print('ref to 5, repr(x) =', repr(x))
print('x() =', x())
print('x() is 5 is', x() is 5)
del x
print("done")
