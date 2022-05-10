import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
a = []
a.append(a)
w = weakref.ref(a)
gc.collect()
print w()

# Test gc.collect()
a = []
a.append(a)
w = weakref.ref(a)
del a
gc.collect()
print w()

# Test gc.collect()
a = []
a.append(a)
w = weakref.ref(a)
del a[0]
gc.collect()
print w()

# Test gc.collect()
a = []
a.append(a)
w = weakref.ref(a)
del a[0][0]
gc.collect()
print w()

# Test gc.collect()
a = []
a.append(a)
w = weakref.ref(a)
del a[0][0][0]
gc.collect()
print w()

# Test gc.collect()
a = []
a.append(a)
w = weakref.ref(a)
del a[0][0][0][0
