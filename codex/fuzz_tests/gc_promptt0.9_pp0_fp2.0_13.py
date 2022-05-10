import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() works and that DEBUG_COLLECTABLE is not
# triggered before the weakref supporting objects are gc'd.
gc.collect(); gc.collect(); gc.collect()

class A:
    p = None

a = A()
aref = weakref.ref(a, _dispose)
a.p = aref
del aref
del a
# Bad things happen if gc.get_referrers is called here: Python crashes.
# This used to be the case if _dispose had been called and then a
# DEBUG_COLLECTABLE debug hook had been triggered.

for n in range(100000):   # many iterations to exercise the bad case
    a = A()
    aref = weakref.ref(a, _dispose)
    a.p = aref
    gc.collect(); gc.collect(); gc.collect()
    del a
    gc.collect(); gc.collect(); gc.collect()
del aref
gc.collect(); gc.collect(); gc.collect()

#### Test that DEBUG_COLLECTABLE is
