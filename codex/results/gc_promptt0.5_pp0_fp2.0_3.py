import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

def f():
    l = []
    l.append(l)
    del l

def g():
    l = []
    l.append(l)
    return l

def h():
    l = []
    l.append(l)
    return weakref.ref(l)

def check_collectable(r, collectable):
    gc.collect()
    assert gc.is_tracked(r) == collectable

for i in range(10):
    f()
    g()
    check_collectable(h(), False)

gc.collect()
check_collectable(h(), True)
