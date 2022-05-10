import weakref
# Test weakref.ref(obj)
# Test weakref.proxy(obj)
# Test weakref.getweakrefcount(obj)
# Test weakref.getweakrefs(obj)
# Test weakref.finalize(obj, callback)
# Test weakref.WeakKeyDictionary()
# Test weakref.WeakValueDictionary()
# Test weakref.WeakSet()

class Foo:
    pass

def callback(obj):
    print("callback:", obj)

def test_weakref():
    f = Foo()
    r = weakref.ref(f)
    p = weakref.proxy(f)
    assert r() is f
    assert p is f
    assert weakref.getweakrefcount(f) == 2
    assert weakref.getweakrefs(f) == [r, p]
    #
    f2 = Foo()
    r2 = weakref.finalize(f2, callback)
    assert weakref.getweakrefcount(f2) == 2
