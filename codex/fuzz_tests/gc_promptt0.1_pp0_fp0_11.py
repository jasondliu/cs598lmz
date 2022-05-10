import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo(object):
    pass

def bar():
    o = Foo()
    o.x = o
    o.y = o
    o.z = o
    o.t = o
    o.u = o
    o.v = o
    o.w = o
    o.a = o
    o.b = o
    o.c = o
    o.d = o
    o.e = o
    o.f = o
    o.g = o
    o.h = o
    o.i = o
    o.j = o
    o.k = o
    o.l = o
    o.m = o
    o.n = o
    o.o = o
    o.p = o
    o.q = o
    o.r = o
    o.s = o
    return o

def test_collect():
    # Test gc.collect()
    gc.collect()
    gc.collect()
    gc.collect()
    gc.collect()
    g
