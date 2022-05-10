import weakref
# Test weakref.ref()

class Foo(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%s)' % self.name

def test_ref():
    foo = Foo('foo')
    foo_ref = weakref.ref(foo)
    print(foo_ref)
    print(foo_ref())
    print(foo_ref() is foo)
    print(foo_ref() is None)
    del foo
    print(foo_ref() is None)

test_ref()

# Test weakref.proxy()

def test_proxy():
    foo = Foo('foo')
    foo_proxy = weakref.proxy(foo)
    print(foo_proxy)
    print(foo_proxy.name)
    print(foo_proxy is foo)
    print(foo_proxy is None)
    del foo
    print(foo_proxy is None)

test_proxy()

# Test weakref.WeakKeyDictionary()

