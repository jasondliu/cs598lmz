import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#gc.collect()

# Test del
#del a
#del b
#del c

# Test gc.collect()
#gc.collect()

# Test weakref
w = weakref.ref(a)
print w
# Test gc.collect()
gc.collect()
print w
# Test del
del a
gc.collect()
print w
