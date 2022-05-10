import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs.

class C:
    pass

class D:
    pass

def f():
    o = C()
    p = D()
    o.p = p
    p.o = o
    wr = weakref.ref(o)
    wrp = weakref.ref(p)
    del o
    del p
    print wr() is None, wrp() is None
    #print gc.collect()
    gc.collect()
    print wr() is None, wrp() is None

f()
f()
