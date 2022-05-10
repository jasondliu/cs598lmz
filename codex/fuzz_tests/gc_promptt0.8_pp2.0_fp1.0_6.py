import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() w/o cyclic trash
gc.collect()
check(gc.DEBUG_COLLECTABLE | gc.DEBUG_UNCOLLECTABLE, 0)

# Test gc.collect() with a cyclic trash can
def f():
    l = [L(), L()]
    ll = [l, l]
    del l, ll
    check(gc.DEBUG_COLLECTABLE | gc.DEBUG_UNCOLLECTABLE, 0)
f()
gc.collect()
check(gc.DEBUG_COLLECTABLE | gc.DEBUG_UNCOLLECTABLE, 0)

# Test gc.collect() with an uncollectable trash can
def f():
    l = [L(), L()]
    l.append(l)
    del l
    check(gc.DEBUG_COLLECTABLE | gc.DEBUG_UNCOLLECTABLE, 3)
f()
gc.collect()
check(gc.DEBUG_COLLECTABLE | gc.DEBUG_UNCOLLECTABLE, 3)

# Test gc.collect() with a finalizer
def f():
    L()
    check
