import weakref
# Test weakref.ref(L)
def test_weakref_ref_list():
    l = [1, 2, 3]
    r = weakref.ref(l)
    assert r() is l
    assert r()[0] == 1
    l.append(4)
    assert r()[3] == 4
    del l
    assert r() is None
# Test weakref.ref(D)
def test_weakref_ref_dict():
    d = {1: 2}
    r = weakref.ref(d)
    assert r() is d
    assert r()[1] == 2
    d[2] = 3
    assert r()[2] == 3
    del d
    assert r() is None
# Test weakref.ref(S)
def test_weakref_ref_set():
    s = set([1, 2, 3])
    r = weakref.ref(s)
    assert r() is s
    assert r() == s
    s.add(4)
    assert r() == s
    del s
    assert r() is None
#
