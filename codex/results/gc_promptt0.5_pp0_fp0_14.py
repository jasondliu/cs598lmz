import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() without any uncollectable objects.
# This should collect all collectable objects.
gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect()

# Test gc.collect() with uncollectable objects that are part of a reference
# cycle.
class A:
    pass
a = A()
b = A()
a.b = b
b.a = a
del a, b
gc.collect()
# This should collect all collectable objects.
gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect()

# Test gc.collect() with uncollectable objects that are not part of a
# reference cycle.
class A:
    pass
a = A()
b = A()
a.b = b
del a, b
gc.collect()
# This should collect all collectable objects.
gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect()

# Test gc.collect() with an object that has a __
