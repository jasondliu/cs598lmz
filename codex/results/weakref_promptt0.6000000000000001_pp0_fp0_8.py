import weakref
# Test weakref.ref(obj)
# Test weakref.proxy(obj)
# Test weakref.getweakrefcount(obj)
# Test weakref.getweakrefs(obj)
# Test weakref.ref(obj, callback)
# Test weakref.WeakSet()
# Test weakref.WeakKeyDictionary()
# Test weakref.WeakValueDictionary()

class Foo(object):
    pass

class Foo2(object):
    def __del__(self):
        print "del Foo2"

class Bar(object):
    def __init__(self):
        self.foo = Foo()

class Bar2(object):
    def __init__(self):
        self.foo = Foo2()

class Bar3(object):
    pass

def callback(ref):
    print "callback", ref

def test_ref():
    # Test weakref.ref(obj)
    o = Foo()
    r = weakref.ref(o)
    assert r() is o
    assert weakref.getweakrefcount(o) == 1
    assert weakref.
