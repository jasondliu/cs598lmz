import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect with a cyclic trash can that has no __del__ method.
def f():
    l = []
    l.append(l)
    return weakref.ref(l)
r = f()
r() is None
gc.collect()
r()
gc.collect()
r() is None
# Now make the trash can uncollectable by having a __del__ method.
def g():
    l = []
    def del_l(l=l):
        l = 42
    l.append(l)
    return weakref.ref(l, del_l)
r = g()
r() is None
gc.collect()
r()
gc.collect()
r() is None
