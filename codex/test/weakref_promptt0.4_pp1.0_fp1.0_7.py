import weakref
# Test weakref.ref()
import weakref

class Foo(object):
    pass

class Bar(object):
    pass

def test_ref():
    f = Foo()
    r = weakref.ref(f)
    assert r() is f
    assert r.__call__() is f
    assert r() is not None

    f = None
    assert r() is None
    assert r.__call__() is None
    assert r() is None

def test_proxy():
    f = Foo()
    p = weakref.proxy(f)
    assert p.__str__() == '<weakproxy object at 0x%x; to ' \
           '%r at 0x%x>' % (id(p), Foo, id(f))
    assert p.__repr__() == '<weakproxy object at 0x%x; to ' \
           '%r at 0x%x>' % (id(p), Foo, id(f))
    assert p.__hash__() == id(f)
    assert p.__nonzero__() is True
