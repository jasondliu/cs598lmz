import weakref
# Test weakref.ref() with a custom object.

class Foo(object):
    pass

class Bar(object):
    pass

class FooBar(object):
    pass

def test_weakref_with_custom_object():
    foo = Foo()
    foo_ref = weakref.ref(foo)
    assert foo_ref() is foo
    del foo
    assert foo_ref() is None
    bar = Bar()
    bar_ref = weakref.ref(bar)
    assert bar_ref() is bar
    del bar
    assert bar_ref() is None
    foobar = FooBar()
    foobar_ref = weakref.ref(foobar)
    assert foobar_ref() is foobar
    del foobar
    assert foobar_ref() is None
