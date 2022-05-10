import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

for c in [A, B, C, D]:
    a = c()
    a.a = a
    a.b = a
    a.c = a
    a.d = a
    a.e = a
    a.f = a
    a.g = a
    a.h = a
    a.i = a
    a.j = a
    a.k = a
    a.l = a
    a.m = a
    a.n = a
    a.o = a
    a.p = a
    a.q = a
    a.r = a
    a.s = a
    a.t = a
    a.u = a
    a.v = a
    a.w = a
    a.x = a
    a.y = a
    a.z = a
    a.aa = a
    a.bb
