import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs

class Foo:
    pass

class Bar:
    pass

def test():
    f = Foo()
    b = Bar()
    f.b = b
    b.f = f
    wf = weakref.ref(f)
    wb = weakref.ref(b)
    del f, b
    gc.collect()
    assert wf() is None
    assert wb() is None

for i in range(10):
    test()

print "OK"
