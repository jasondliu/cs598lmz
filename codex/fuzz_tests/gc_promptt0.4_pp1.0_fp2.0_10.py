import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() before and after weakref creation.
gc.collect()
gc.collect()

class A:
    pass

o = A()
r = weakref.ref(o)

gc.collect()
gc.collect()

del o

gc.collect()
gc.collect()

del r

gc.collect()
gc.collect()

# Test gc.collect() before and after weakref creation.
gc.collect()
gc.collect()

class A:
    pass

o = A()
r = weakref.ref(o)

gc.collect()
gc.collect()

del o

gc.collect()
gc.collect()

del r

gc.collect()
gc.collect()

# Test gc.collect() before and after weakref creation.
gc.collect()
gc.collect()

class A:
    pass

o = A()
r = weakref.ref(o)

gc.collect()
gc.collect()

del o

gc.collect()
gc.collect()

del r

