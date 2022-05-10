import weakref
# Test weakref.ref() and weakref.proxy()

import weakref

class Foo:
    pass

def test_ref():
    foo = Foo()
    foo_ref = weakref.ref(foo)
    assert foo_ref() is foo
    del foo
    assert foo_ref() is None

def test_proxy():
    foo = Foo()
    foo_proxy = weakref.proxy(foo)
    assert foo_proxy is foo
    del foo
    raises(ReferenceError, getattr, foo_proxy, 'bar')

def test_proxy_call():
    def foo():
        pass
    foo_proxy = weakref.proxy(foo)
    assert foo_proxy() is None

def test_proxy_call_args():
    def foo(a, b):
        return a, b
    foo_proxy = weakref.proxy(foo)
    assert foo_proxy(1, 2) == (1, 2)

def test_proxy_call_kwargs():
    def foo(a, b):
        return a, b
    foo_proxy = weakref.proxy
