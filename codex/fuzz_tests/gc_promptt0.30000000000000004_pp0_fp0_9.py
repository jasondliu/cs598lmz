import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class C:
    pass

def f():
    c = C()
    c.x = c
    c.y = c
    c.z = c
    c.t = c
    c.u = c
    c.v = c
    c.w = c
    c.a = c
    c.b = c
    c.c = c
    c.d = c
    c.e = c
    c.f = c
    c.g = c
    c.h = c
    c.i = c
    c.j = c
    c.k = c
    c.l = c
    c.m = c
    c.n = c
    c.o = c
    c.p = c
    c.q = c
    c.r = c
    c.s = c
    c.t = c
    c.u = c
    c.v = c
    c.w = c
    c.a = c
    c.b = c
    c.c = c
    c.
