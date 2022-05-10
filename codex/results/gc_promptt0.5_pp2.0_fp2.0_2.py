import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() before uncollectable objects are detected
gc.collect()

class A:
    pass
a = A()
a.b = A()
a.b.a = a
del a

gc.collect()

# Test gc.collect() after uncollectable objects are detected
a = A()
a.b = A()
a.b.a = a
del a

gc.collect()
