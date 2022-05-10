import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    pass

def bar():
    print "bar"

f = Foo()
f.x = Foo()
f.x.a = weakref.ref(f)
f.x.b = weakref.ref(f)
f.x.c = weakref.ref(f)
f.x.d = weakref.ref(f)
f.x.e = weakref.ref(f)
f.x.f = weakref.ref(f)
f.x.g = weakref.ref(f)
f.x.h = weakref.ref(f)
f.x.i = weakref.ref(f)
f.x.j = weakref.ref(f)
f.x.k = weakref.ref(f)
f.x.l = weakref.ref(f)
f.x.m = weakref.ref(f)
f.x.n = weakref.ref(f)
f.x.o = weakref.ref(f)
f.x.p = weakref.ref(
