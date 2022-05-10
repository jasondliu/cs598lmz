import weakref
# Test weakref.ref() and weakref.proxy()

# Test weakref.ref()

class Foo(object):
    pass

def test_ref():
    f = Foo()
    r = weakref.ref(f)
    assert r() is f
    assert r() is not None
    del f
    assert r() is None

def test_ref_callback():
    f = Foo()
    def callback(r):
        callback.called = True
    callback.called = False
    r = weakref.ref(f, callback)
    assert not callback.called
    del f
    assert callback.called

def test_ref_callback_exception():
    f = Foo()
    def callback(r):
        callback.called = True
        raise Exception
    callback.called = False
    r = weakref.ref(f, callback)
    assert not callback.called
    del f
    assert callback.called

def test_ref_callback_weakref_removed():
    f = Foo()
    def callback(r):
        callback.called = True
    callback.called
