import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    pass

def bar():
    f = Foo()
    f.x = 1
    f.y = 2
    f.z = 3
    f.t = 4
    f.u = 5
    f.v = 6
    f.w = 7
    f.a = 8
    f.b = 9
    f.c = 10
    f.d = 11
    f.e = 12
    f.f = 13
    f.g = 14
    f.h = 15
    f.i = 16
    f.j = 17
    f.k = 18
    f.l = 19
    f.m = 20
    f.n = 21
    f.o = 22
    f.p = 23
    f.q = 24
    f.r = 25
    f.s = 26
    f.t = 27
    f.u = 28
    f.v = 29
    f.w = 30
    f.x = 31
    f.y = 32
    f.z = 33
    f.
