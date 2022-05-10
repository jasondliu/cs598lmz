import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

def f():
    l = [weakref.ref(i) for i in range(10)]
    gc.collect()
    return l

def g():
    l = [weakref.ref(i) for i in range(10)]
    del l
    gc.collect()

def h():
    l = [weakref.ref(i) for i in range(10)]
    gc.collect()
    del l

f()
g()
h()

# Test gc.get_referrers()

def f():
    l = [weakref.ref(i) for i in range(10)]
    gc.collect()
    return l

def g():
    l = [weakref.ref(i) for i in range(10)]
    del l
    gc.collect()

def h():
    l = [weakref.ref(i) for i in range(10)]
    gc.collect()
    del l

gc.set_debug(gc.DEBUG_COLLECTABLE | gc.DEBUG_
