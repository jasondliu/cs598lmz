import weakref
# Test weakref.ref() on built-in types.
import _weakref

class Foo:
    pass

class Foo2(Foo):
    pass

class Bar:
    pass

def test_ref(t, arg, create_func=weakref.ref):
    r = create_func(arg)
    assert r() is arg
    assert type(r) is t
    del arg
    assert r() is None

def test_proxy(t, arg, create_func=weakref.proxy):
    p = create_func(arg)
    assert type(p) is t
    assert p is arg
    assert repr(p) == repr(arg)
    assert p == arg
    if hasattr(arg, '__hash__'):
        assert hash(p) == hash(arg)
    try:
        del p.__dict__
    except TypeError:
        pass
    else:
        assert 0, "shouldn't be able to delete __dict__ of weak proxy"
    del arg
    try:
        p is None
    except ReferenceError:
        pass
   
