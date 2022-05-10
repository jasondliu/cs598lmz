import weakref
# Test weakref.ref(x) == weakref.ref(x)

class Foo(object):
    pass

def test_ref_eq():
    f = Foo()
    r1 = weakref.ref(f)
    r2 = weakref.ref(f)
    assert r1 == r2
    assert r1 is not r2
    assert r1() is r2()
    assert r1() is f

def test_ref_ne():
    f1 = Foo()
    f2 = Foo()
    r1 = weakref.ref(f1)
    r2 = weakref.ref(f2)
    assert r1 != r2
    assert r1() is not r2()
    assert r1() is f1
    assert r2() is f2

def test_ref_eq_other():
    f = Foo()
    r = weakref.ref(f)
    assert r != 42
    assert 42 != r

def test_ref_hash():
    f = Foo()
    r = weakref.ref(f)
    assert hash(r) ==
