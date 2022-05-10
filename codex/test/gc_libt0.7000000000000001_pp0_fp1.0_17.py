import gc, weakref

def test_weak_refs():
    # Test that weakrefs are supported
    class Test:
        pass

    obj = Test()
    obj.x = 1
    obj.y = 2
    obj.z = 3
    p = weakref.proxy(obj)
    assert p.x == 1
    assert p.y == 2
    assert p.z == 3

    obj2 = Test()
    obj2.x = 4
    obj2.y = 3
    obj2.z = 2
    p2 = weakref.proxy(obj)
    assert p2.x == 1
    assert p2.y == 2
    assert p2.z == 3

def test_weak_ref_lifetime():
    # Test that weakrefs can die
    class Test:
        pass

    obj = Test()
    obj.x = 1
    obj.y = 2
    obj.z = 3
    p = weakref.proxy(obj)
    assert p.x == 1
    assert p.y == 2
    assert p.z == 3
    obj
