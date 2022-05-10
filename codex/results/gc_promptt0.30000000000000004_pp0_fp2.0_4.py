import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class A:
    pass

def f():
    a = A()
    a.a = a
    a.b = A()
    a.b.a = a
    a.b.b = a.b
    a.b.c = a.b.a
    a.b.d = a.b.b
    a.b.e = a.b.c
    a.b.f = a.b.d
    a.b.g = a.b.e
    a.b.h = a.b.f
    a.b.i = a.b.g
    a.b.j = a.b.h
    a.b.k = a.b.i
    a.b.l = a.b.j
    a.b.m = a.b.k
    a.b.n = a.b.l
    a.b.o = a.b.m
    a.b.p = a.b.n
    a.b.q = a.b.o
    a.b
