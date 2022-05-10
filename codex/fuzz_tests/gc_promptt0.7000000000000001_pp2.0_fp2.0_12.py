import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
def f():
    a = weakref.ref(Test())
    print(gc.collect())
    b = weakref.ref(Test())
    print(gc.collect())
    del a
    print(gc.collect())
    del b
    print(gc.collect())
f()
