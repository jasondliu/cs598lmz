import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() when there is a cycle without a CREATED finalizer.
a = []
a.append(a)
gc.collect()

# Test gc.collect() when there is a cycle with a CREATED finalizer.
a = []
f = Finalizer(a, lambda: 42, a)
a.append(a)
gc.collect()

# Test gc.collect() for an object with a finalizer that has a cycle.
a = []
Finalizer(a, lambda: 42, a)
del a
gc.collect()

# Test gc.collect() when there is an object with a finalizer, and a cycle
# including that object.  This exercises the code that ensures that we
# don't add the finalizer object twice to the list of objects with
# finalizers.
a = []
Finalizer(a, lambda: 42, a)
a.append(a)
del a
gc.collect()

# Test gc.collect() when there is an object with a finalizer, and a cycle
# including that object, but the finalizer is already dead.
a = []

