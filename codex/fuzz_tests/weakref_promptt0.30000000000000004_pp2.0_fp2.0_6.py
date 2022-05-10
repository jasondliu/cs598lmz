import weakref
# Test weakref.ref()

class Foo(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%s)' % self.name

def test_ref():
    f = Foo('bar')
    r = weakref.ref(f)
    assert r() is f
    assert r().name == 'bar'
    del f
    assert r() is None

def test_callable():
    f = Foo('bar')
    r = weakref.ref(f)
    assert r() is f
    assert r().name == 'bar'
    del f
    raises(ReferenceError, "r()")

def test_hash():
    f = Foo('bar')
    r = weakref.ref(f)
    assert hash(r) == hash(f)
    del f
    raises(ReferenceError, "hash(r)")

def test_call_after_deletion():
    f = Foo('bar')
    r = weakref.ref(f)
    del f

