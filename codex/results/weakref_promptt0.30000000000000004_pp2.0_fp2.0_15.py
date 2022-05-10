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
    assert str(r) == '<weakref at 0x%x; to ' % id(r) + repr(f) + '>'
    assert repr(r) == '<weakref at 0x%x; to ' % id(r) + repr(f) + '>'
    assert r == r
    assert r != 42
    assert r != weakref.ref(Foo('f'))
    assert hash(r) == hash(r)
    assert hash(r) == hash(weakref.ref(f))
    assert hash(r) != hash(42)
    assert hash(r) != hash(weakref.ref(Foo('f')))
    del f
    assert r
