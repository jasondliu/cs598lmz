import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo(object):
    pass

class Bar(object):
    pass

def test_collect():
    # l = []
    # l.append(l)
    f = Foo()
    f2 = Foo()
    f.f = f2
    f2.f = f

    ref = weakref.ref(f)
    assert ref() is f
    del f
    del f2
    gc.collect()
    assert ref() is None
    assert gc.collect() == 0

# test_collect()
def test_get_referents():
    f = Foo()
    f2 = Foo()
    f.f = f2
    f2.f = f
    l = [f, f2]
    assert gc.get_referents(l) == [f, f2]
    assert gc.get_referents(l, Foo) == [f, f2]
    assert gc.get_referents(l, Bar) == []

# test_get_referents()

#
