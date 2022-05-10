import weakref
# Test weakref.ref() and weakref.proxy()

class C:
    pass

def test_basic():
    c = C()
    r = weakref.ref(c)
    assert r() is c
    c.foo = 12
    assert r().foo == 12
    assert r() is not None
    del c
    assert r() is None

    # test the proxy
    c = C()
    p = weakref.proxy(c)
    assert p.foo == 12
    c.foo = 10
    assert p.foo == 10
    assert p is not c
    del c
    try:
        p.foo
    except ReferenceError:
        pass
    else:
        print("weakref.proxy did not raise ReferenceError")

    # test the callback
    c = C()
    l = []
    def f(x):
        l.append(x)
    r = weakref.ref(c, f)
    assert r() is c
    del c
    assert l == [c]

def test_basic_nocallback():
    c = C()
