import weakref
# Test weakref.ref(x) == weakref.ref(x)

class Foo:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%r)' % self.name

def test_basic():
    f = Foo('one')
    r1 = weakref.ref(f)
    r2 = weakref.ref(f)
    assert r1 == r2
    assert not (r1 != r2)

def test_basic_with_callback():
    l = []
    def callback(r):
        l.append(r)
    f = Foo('one')
    r1 = weakref.ref(f, callback)
    r2 = weakref.ref(f, callback)
    assert r1 == r2
    assert not (r1 != r2)
    del f
    support.gc_collect()
    assert l == [r1]

def test_different():
    f = Foo('one')
    r1 = weakref.ref(f)
    f = Foo
