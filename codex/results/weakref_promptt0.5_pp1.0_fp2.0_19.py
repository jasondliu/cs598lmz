import weakref
# Test weakref.ref.__call__

class C(object):
    pass

def f(o):
    return o

def g():
    pass

def h(o):
    return o

def test_call():
    c = C()
    r = weakref.ref(c, f)
    assert r() is c
    r = weakref.ref(c, g)
    assert r() is None
    r = weakref.ref(c, h)
    assert r() is c
    c = None
    assert r() is None

def test_call_builtin():
    # Issue #14071: calling a weakref to a built-in type should return the
    # object, not the wrapper.
    c = C()
    r = weakref.ref(c, f)
    assert r() is c
    r = weakref.ref(c, g)
    assert r() is None
    r = weakref.ref(c, h)
    assert r() is c
    c = None
    assert r() is None

def test_call_
