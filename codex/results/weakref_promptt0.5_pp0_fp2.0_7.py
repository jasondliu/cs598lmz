import weakref
# Test weakref.ref()

class Foo:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Foo({!r})'.format(self.name)

def test_foo(func):
    # Create a Foo instance
    i = Foo('i')
    # Get a weak reference to it
    r = func(i)
    # Check that the weakref is valid
    assert r() is i
    # Delete the Foo instance
    del i
    # Check that the weakref is now dead
    assert r() is None

def test_foo_weakref():
    test_foo(weakref.ref)

# Test weakref.proxy()

def test_foo_proxy():
    test_foo(weakref.proxy)

def test_proxy_repr():
    assert repr(weakref.proxy(Foo('i'))) == '<weakproxy at 0x{:x} to Foo(None)>'.format(id(Foo('i')))

# Test weakref.finalize()


