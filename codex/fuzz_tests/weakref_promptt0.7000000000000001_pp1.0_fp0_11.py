import weakref
# Test weakref.ref(obj)

def test_ref():
    class Foo:
        pass
    f = Foo()
    assert weakref.ref(f)() is f
    assert repr(weakref.ref(f)) == "<weakref at 0x%x; to 'Foo' at 0x%x>" % (id(weakref.ref(f)), id(f))

def test_printable():
    class Foo:
        pass
    f = Foo()
    assert weakref.ref(f)() is f
    assert repr(weakref.ref(f)) == "<weakref at 0x%x; to 'Foo' at 0x%x>" % (id(weakref.ref(f)), id(f))

def test_callable():
    class Foo(object):
        def __call__(self):
            return 1
    f = Foo()
    assert weakref.ref(f)()() == 1
    assert repr(weakref.ref(f)) == "<weakref at 0x%x; to 'Foo' at 0x%x>" % (id(weakref
