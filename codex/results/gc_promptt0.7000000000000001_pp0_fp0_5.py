import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()
# Test gc.garbage
class A: pass
a = A()
a.b = A()
a.b.a = a
a.b.b = A()
a.b.b.a = a
a.b.b.b = a.b
a.b.b.c = A()
a.b.b.c.a = a.b.b
a.b.b.c.b = a.b
a.b.b.c.c = a
a.b.b.c.d = a.b.b.c
a.b.b.c.e = a.b.b.c
a.b.b.c.f = a.b.b.c
a.b.b.c.g = a.b.b.c
a.b.b.c.h = a.b.b.c
a.b.b.c.i = a.b.b.c
# Test gc.get_debug()
gc.get_debug()
# Test gc.set
