import weakref
# Test weakref.ref(a) and weakref.proxy(a)
#
# Test weakref.WeakValueDictionary()
#
# Test weakref.WeakKeyDictionary()
#
# Test weakref.WeakSet()
#

class Foo:
    pass

def test_basic(obj):
    # Test weakref.ref(obj)
    a = weakref.ref(obj)
    assert a() is obj

    # Test weakref.proxy(obj)
    b = weakref.proxy(obj)
    assert b is obj

    # Test weakref.getweakrefcount(obj)
    n = weakref.getweakrefcount(obj)
    assert n >= 1

    # Test weakref.getweakrefs(obj)
    r = weakref.getweakrefs(obj)
    assert len(r) >= 1
    assert a in r

