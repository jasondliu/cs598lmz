import weakref
# Test weakref.ref(x)
class Foo:
    def __init__(self, x):
        self.x = x
    def __repr__(self):
        return 'Foo(%r)' % self.x

def test():
    f = Foo(42)
    r = weakref.ref(f)
    assert r() is f
    assert r().x == 42
    print(r())
    del f
    assert r() is None
    try:
        r().x
    except ReferenceError:
        pass
    else:
        raise AssertionError

test()
