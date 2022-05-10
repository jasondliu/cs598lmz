import weakref
# Test weakref.ref(obj)
def test_weakref_ref():
    class Foo:
        pass
    a = Foo()
    assert isinstance(weakref.ref(a), weakref.ReferenceType)
    assert weakref.ref(a)() is a
    raises(TypeError, weakref.ref, 1)
    raises(TypeError, weakref.ref, "foo")
    raises(TypeError, weakref.ref, u"foo")
    raises(TypeError, weakref.ref, [])
    raises(TypeError, weakref.ref, {})
    raises(TypeError, weakref.ref, ())
    raises(TypeError, weakref.ref, object)
    raises(TypeError, weakref.ref, object())
    raises(TypeError, weakref.ref, object)
    raises(TypeError, weakref.ref, object())
    raises(TypeError, weakref.ref, object)
    raises(TypeError, weakref.ref, object())

# Test weakref.proxy(obj)
def test_weakref_proxy():
    class Foo:
       
