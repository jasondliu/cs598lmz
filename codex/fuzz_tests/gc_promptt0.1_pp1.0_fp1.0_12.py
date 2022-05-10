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
    a.x = c
    a.y = weakref.ref(a)
    a.z = weakref.ref(a)
    a.t = weakref.ref(a)
    a.u = weakref.ref(a)
    a.v = weakref.ref(a)
    a.w = weakref.ref(a)
    a.x = weakref.ref(a)
    a.y = weakref.ref(a)
    a.z = weakref.ref(a)
    a.t = weakref.ref(a)
    a.u = weakref.ref(a)
    a.v = weakref.ref(a)
    a.w = weakref.ref(a)
    a.x = weakref.ref(a)
    a.y
