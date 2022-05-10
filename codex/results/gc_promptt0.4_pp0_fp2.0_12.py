import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() on a weakref proxy.

class C:
    pass

def f():
    c = C()
    c.x = c
    p = weakref.proxy(c)
    c = None
    gc.collect()
    return p.x

f()
gc.collect()
gc.collect()
