import weakref
# Test weakref.ref(obj)
# Test weakref.proxy(obj)
# Test weakref.getweakrefcount(obj)
# Test weakref.getweakrefs(obj)
# Test weakref.WeakKeyDictionary
# Test weakref.WeakValueDictionary
# Test weakref.WeakSet
# Test weakref.finalize(obj, callback, *args, **kwargs)
# Test weakref.ref(obj, callback, *args, **kwargs)
# Test weakref.WeakMethod(method, callback, *args, **kwargs)
# Test weakref.WeakMethodProxy(method, callback, *args, **kwargs)

class Foo(object):
    pass

class Bar(object):
    pass

class Baz(object):
    pass

def callback(ref):
    print("callback", ref)

def test_ref():
    foo = Foo()
    ref = weakref.ref(foo)
    assert ref() is foo
    del foo
    assert ref() is None

def test_proxy():
    foo = Foo()
    bar = Bar()
   
