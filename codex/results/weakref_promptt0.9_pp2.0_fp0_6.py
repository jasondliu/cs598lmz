import weakref
# Test weakref.ref callable.


class C:

    def __init__(self):
        self.data = list(range(10))


def test_callable():
    o = C()
    o.f = o.data.append
    r = weakref.ref(o)
    wr = weakref.ref(o.f, r)
    eq = r() is o
    assert r() is not None
    assert r() is o
    assert wr() is o.f
    r().data.append(10)
    r().f(11)
    assert r().data == list(range(12))
    del o
    try:
        r().data
    except ReferenceError:
        pass
    else:
        assert False
# bug 832084
# Test weakref.ref to bound methods.  Python's reference counting
# doesn't collect instances with a bound method, so we have to test
# this carefully, lest the test itself introduce a reference.


class C:

    def __init__(self):
        self.data = list(range(10))

    def f(
