import weakref
# Test weakref.ref() and weakref.proxy()

import weakref

class Foo:
    pass

def test_ref():
    f = Foo()
    r = weakref.ref(f)
    assert r() is f
    assert r() is not None
    del f
    assert r() is None

def test_proxy():
    f = Foo()
    p = weakref.proxy(f)
    assert p is f
    assert p is not None
    del f
    try:
        p.foo
    except ReferenceError:
        pass
    else:
        raise Exception("expected ReferenceError")

def test_proxy_callable():
    f = Foo()
    p = weakref.proxy(f)
    assert p() is None
    f.__call__ = lambda: 42
    assert p() == 42

def test_proxy_callable_exception():
    f = Foo()
    p = weakref.proxy(f)
    f.__call__ = lambda: 42/0
