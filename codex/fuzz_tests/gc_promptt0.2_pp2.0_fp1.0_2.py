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

class E:
    pass

for c in [A, B, C, D, E]:
    a = c()
    a.x = c
    a.y = c
    a.z = c
    a.t = c
    a.u = c
    a.v = c
    a.w = c
    a.r = c
    a.s = c
    a.o = c
    a.p = c
    a.q = c
    a.m = c
    a.n = c
    a.l = c
    a.k = c
    a.j = c
    a.i = c
    a.h = c
    a.g = c
    a.f = c
    a.e = c
    a.d = c
    a.c = c
    a.b = c
    a.a = c
   
