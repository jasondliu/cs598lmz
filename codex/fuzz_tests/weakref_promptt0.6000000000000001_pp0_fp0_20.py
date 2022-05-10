import weakref
# Test weakref.ref(None)

class Foo(object):
    pass


def test_none():
    f = Foo()
    r = weakref.ref(f)
    assert r() is f
    del f
    assert r() is None
    r = weakref.ref(None)
    assert r() is None
    r = weakref.ref(42)
    assert r() == 42
    r = weakref.ref(3.14)
    assert r() == 3.14
    r = weakref.ref('abc')
    assert r() == 'abc'
    r = weakref.ref(u'abc')
    assert r() == u'abc'
    r = weakref.ref((1, 2, 3))
    assert r() == (1, 2, 3)
    r = weakref.ref([1, 2, 3])
    assert r() == [1, 2, 3]


def test_del_on_weakref():
    f = Foo()
    # deleting the weakref should not affect the referent
    r = weakref.ref(f)

