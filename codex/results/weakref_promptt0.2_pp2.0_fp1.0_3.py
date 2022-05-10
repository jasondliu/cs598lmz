import weakref
# Test weakref.ref() and weakref.proxy()

class Foo(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%r)' % self.name

def test_ref():
    f = Foo('f')
    r = weakref.ref(f)
    assert r() is f
    assert r().name == 'f'
    assert str(r) == 'Foo(f)'
    assert repr(r) == '<weakref at %#x; to ' % id(r) + 'Foo(f)>'
    f = None
    assert r() is None
    assert str(r) == 'None'
    assert repr(r) == '<weakref at %#x; dead>' % id(r)

def test_proxy():
    f = Foo('f')
    p = weakref.proxy(f)
    assert p is f
    assert p.name == 'f'
    assert str(p) == 'Foo(f)'
    assert repr(
