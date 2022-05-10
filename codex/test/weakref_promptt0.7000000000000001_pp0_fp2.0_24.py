import weakref
# Test weakref.ref(x) == weakref.ref(x)

import gc

def test_eq_basic():
    # Issue #17171: The result of a weakref.ref() call should always compare
    # equal to itself, even if the referent is later garbage collected.
    class A:
        pass
    a = A()
    r = weakref.ref(a)
    assert r == r
    del a
    gc.collect()
    assert r == r
    class B(object):
        pass
    b = B()
    r = weakref.ref(b)
    assert r == r
    del b
    gc.collect()
    assert r == r

def test_eq_against_normal():
    # Issue #17171: The result of a weakref.ref() call should never compare
    # equal to a normal reference to the same object.
    class A:
        pass
    a = A()
    r = weakref.ref(a)
    assert r != a

    class B(object):
        pass
    b = B()
   
