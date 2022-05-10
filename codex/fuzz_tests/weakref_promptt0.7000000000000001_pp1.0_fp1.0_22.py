import weakref
# Test weakref.ref(callable)

global_l = [1]
def f(l):
    return l[0]

l = []
def g():
    return l[0]

def test_ref_class():
    r = weakref.ref(f, global_l)
    assert r() == 1
    global_l[0] = 5
    assert r() == 5
    del global_l
    py.test.raises(TypeError, "r()")

def test_ref_function():
    r = weakref.ref(g)
    l.append(5)
    assert r() == 5
    l[0] = 10
    assert r() == 10
    del l
    py.test.raises(TypeError, "r()")

def test_ref_exception():
    py.test.raises(TypeError, weakref.ref, 42)
    py.test.raises(TypeError, weakref.ref, None)
    py.test.raises(TypeError, weakref.ref, '')
    py.test.
