import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs.

class C(object):
    pass

def f():
    x = C()
    x.a = x
    wr = weakref.ref(x)
    del x
    return wr

wr = f()
gc.collect()
print wr() is None
