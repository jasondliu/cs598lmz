import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
def f():
    class C: pass
    x = C()
    x.a = C()
    x.a.b = x
    x.a.b.c = x.a
    del x.a
    del x

f()
gc.collect()
# Test gc.get_referrers()
def g():
    class C: pass
    x = C()
    x.a = C()
    x.a.b = x
    x.a.b.c = x.a
    del x.a
    del x

g()
gc.collect()
print len(gc.get_referrers(C))
# Test gc.get_referents()
def h():
    class C: pass
    x = C()
    x.a = C()
    x.a.b = x
    x.a.b.c = x.a
    del x.a
    del x

h()
gc.collect()
print len(gc.get_referents(C))
# Test weakref.ref
