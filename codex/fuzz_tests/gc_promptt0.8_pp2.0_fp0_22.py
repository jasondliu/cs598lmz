import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() and gc.is_tracked()
a = list(range(10))
gc.collect()
print(gc.is_tracked(a))
# Test weakref callback
def foo(x):
    print('foo:', x)
w = weakref.ref(a, foo)
del a
gc.collect()
