import weakref
# Test weakref.ref()

class C:
    pass

def test_ref():
    c = C()
    r = weakref.ref(c)
    assert r() is c
    del c
    assert r() is None

def test_ref_callable():
    c = C()
    l = []
    def f(r):
        l.append(1)
    r = weakref.ref(c, f)
    assert r() is c
    del c
    assert r() is None
    assert l == [1]

def test_ref_callable_exception():
    c = C()
    l = []
    def f(r):
        l.append(1)
        raise ValueError
    r = weakref.ref(c, f)
    assert r() is c
    del c
    assert r() is None
    assert l == [1]

def test_ref_callable_error():
    c = C()
    l = []
    def f(r):
        l.append(1)
        raise TypeError
    r
