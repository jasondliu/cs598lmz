import weakref
# Test weakref.ref() and weakref.proxy()

class Foo:
    def __init__(self):
        self.data = [1, 2, 3]

def test_ref():
    foo = Foo()
    ref = weakref.ref(foo)
    assert ref() is foo
    assert ref().data == [1, 2, 3]
    del foo
    assert ref() is None

def test_proxy():
    foo = Foo()
    proxy = weakref.proxy(foo)
    assert proxy.data == [1, 2, 3]
    del foo
    raises(ReferenceError, getattr, proxy, 'data')

def test_callbacks():
    foo = Foo()
    l = []
    def callback(ref):
        l.append(ref)
    ref = weakref.ref(foo, callback)
    assert ref() is foo
    del foo
    assert len(l) == 1
    assert l[0]() is None
    assert ref() is None
    foo = Foo()
    ref = weakref.ref(foo, callback)
    assert ref()
