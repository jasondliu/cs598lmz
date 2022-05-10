import weakref
# Test weakref.ref(self) vs. weakref.proxy(self)


class Foo:

    def __init__(self):
        self.bar = 1
        self.ref = weakref.ref(self)
        self.proxy = weakref.proxy(self)


def test_weakref_ref():
    foo = Foo()
    assert foo.ref() is foo
    assert foo.ref().bar == 1
    assert foo.ref().proxy is foo
    del foo
    assert foo.ref() is None
    assert callable(foo.ref)


def test_weakref_proxy():
    foo = Foo()
    assert foo.proxy is foo
    assert foo.proxy.bar == 1
    assert foo.proxy.proxy is foo
    del foo
    assert foo.proxy() is None
    assert callable(foo.ref)


class Foo2:

    def __init__(self):
        self.bar = 1
        self.ref = weakref.proxy(self)


def test_weakref_proxy_ref():
    foo = Foo2()
    assert foo.ref is
