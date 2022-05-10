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
    a.y = weakref.ref(a)
    a.z = weakref.ref(a)
    a.t = weakref.ref(a)
    a.u = weakref.ref(a)
    a.v = weakref.ref(a)
    a.w = weakref.ref(a)
    a.s = weakref.ref(a)
    a.r = weakref.ref(a)
    a.q = weakref.ref(a)
    a.p = weakref.ref(a)
    a.o = weakref.ref(a)
    a.n = weakref.ref(a)
    a.m = weakref.ref(a)
    a.l = weakref
