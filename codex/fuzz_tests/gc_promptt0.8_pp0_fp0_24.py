import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect on weakref.ref objects
class A:
    pass
a = A()
ra = weakref.ref(a)
del a
gc.collect()
print(gc.get_referrers(ra))
print(gc.collect())
