import weakref
# Test weakref.ref()

class Foo(object):
    pass

def test():
    f = Foo()
    r = weakref.ref(f)
    assert r() is f
    del f
    assert r() is None

test()
print('passed')
