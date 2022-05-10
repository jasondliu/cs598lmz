import weakref
# Test weakref.ref(obj)
# Test weakref.proxy(obj)
# Test weakref.getweakrefcount(obj)
# Test weakref.getweakrefs(obj)
# Test weakref.WeakKeyDictionary
# Test weakref.WeakValueDictionary
# Test weakref.finalize
# Test weakref.WeakSet

class Foo(object):
    pass

def test_ref():
    foo = Foo()
    foo_ref = weakref.ref(foo)
    assert foo_ref() is foo
    del foo
    assert foo_ref() is None

def test_proxy():
    foo = Foo()
    foo_ref = weakref.proxy(foo)
    assert foo_ref is foo
    del foo
    raises(ReferenceError, "foo_ref.bar")

def test_getweakrefcount():
    foo = Foo()
    foo_ref = weakref.ref(foo)
    assert weakref.getweakrefcount(foo) == 1
    assert weakref.getweakrefcount(foo_ref()) == 1
    del foo_ref
    assert
