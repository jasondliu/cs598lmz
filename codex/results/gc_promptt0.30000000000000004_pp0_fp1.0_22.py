import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs
class A:
    pass
a = A()
a.x = A()
a.x.y = A()
a.x.y.z = a
a.x.y.w = a.x
a.x.y.v = a.x.y
a.x.y.u = a.x.y.z
a.x.y.t = a.x.y.w
a.x.y.s = a.x.y.v
a.x.y.r = a.x.y.u
a.x.y.q = a.x.y.t
a.x.y.p = a.x.y.s
a.x.y.o = a.x.y.r
a.x.y.n = a.x.y.q
a.x.y.m = a.x.y.p
a.x.y.l = a.x.y.o
a.x.y.k = a.x.y.n
a.x.y.j = a
