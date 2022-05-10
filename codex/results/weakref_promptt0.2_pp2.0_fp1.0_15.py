import weakref
# Test weakref.ref()

class Foo:
    pass

def test_weakref_ref():
    f = Foo()
    r = weakref.ref(f)
    assert r() is f
    del f
    assert r() is None

def test_weakref_ref_callable():
    f = Foo()
    r = weakref.ref(f, lambda x: None)
    assert r() is f
    del f
    assert r() is None

def test_weakref_ref_type():
    f = Foo()
    r = weakref.ref(f)
    assert type(r) is weakref.ref

def test_weakref_ref_hash():
    f = Foo()
    r = weakref.ref(f)
    assert hash(r) == hash(f)

def test_weakref_ref_eq():
    f = Foo()
    r = weakref.ref(f)
    assert r == f

def test_weakref_ref_ne():
    f = Foo()
    r = weakref.ref(f)
   
