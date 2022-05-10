import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs.

class C(object):
    pass

class D(object):
    pass

def f():
    c = C()
    d = D()
    wr = weakref.ref(c)
    wr2 = weakref.ref(d)
    del c, d
    gc.collect()
    return wr, wr2

wr, wr2 = f()
print wr()
print wr2()
