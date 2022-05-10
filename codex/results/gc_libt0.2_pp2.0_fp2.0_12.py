import gc, weakref

def test_weakref_callback():
    class Foo(object):
        pass

    def callback(ref):
        print "callback called"
        assert ref() is foo

    foo = Foo()
    foo_ref = weakref.ref(foo, callback)
    assert foo_ref() is foo

    del foo
    gc.collect()
    assert foo_ref() is None

def test_weakref_callback_exception():
    class Foo(object):
        pass

    def callback(ref):
        print "callback called"
        assert ref() is foo
        raise ValueError

    foo = Foo()
    foo_ref = weakref.ref(foo, callback)
    assert foo_ref() is foo

    del foo
    gc.collect()
    assert foo_ref() is None

def test_weakref_callback_exception_2():
    class Foo(object):
        pass

    def callback(ref):
        print "callback called"
        assert ref() is foo
        raise ValueError

    foo = Foo()
    foo_ref = weakref
