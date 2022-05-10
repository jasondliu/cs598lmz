import weakref
# Test weakref.ref, weakref.proxy, weakref.getweakrefcount, weakref.getweakrefs

class C:
    pass

def f():
    pass

def test_weakref():
    o = C()
    p = weakref.proxy(o)
    r = weakref.ref(o)
    assert r() is o
    assert p is o
    assert p.__class__ is C
    assert r.__class__ is weakref.ReferenceType
    assert p.x == 1
    p.x = 2
    assert o.x == 2
    assert p.x == 2
    raises(AttributeError, "del p.x")
    raises(TypeError, "p()")
    raises(TypeError, "p(1)")
    raises(TypeError, "p(1,2)")
    raises(TypeError, "p(1,2,3)")
    assert weakref.getweakrefcount(o) == 1
    assert weakref.getweakrefs(o) == [r]
    del o
    assert r() is None
   
