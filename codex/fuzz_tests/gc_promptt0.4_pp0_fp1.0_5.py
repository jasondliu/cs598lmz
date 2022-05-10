import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref to a new-style class instance.

class C(object):
    pass

def check(c):
    if c is not None:
        raise RuntimeError("c is not None")

c = C()
check(c)
w = weakref.ref(c)
check(c)
del c
check(w())
gc.collect()
check(w())
