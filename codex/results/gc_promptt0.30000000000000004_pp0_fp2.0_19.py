import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo(object):
    pass

def bar():
    print 'bar'

f = Foo()
f.x = Foo()
f.x.a = Foo()
f.x.a.b = Foo()
f.x.a.b.c = Foo()
f.x.a.b.c.d = Foo()
f.x.a.b.c.d.e = Foo()
f.x.a.b.c.d.e.f = Foo()
f.x.a.b.c.d.e.f.g = Foo()
f.x.a.b.c.d.e.f.g.h = Foo()
f.x.a.b.c.d.e.f.g.h.i = Foo()
f.x.a.b.c.d.e.f.g.h.i.j = Foo()
f.x.a.b.c.d.e.f.g.h.i.j.k = Foo()
f.x.a.b.c.
