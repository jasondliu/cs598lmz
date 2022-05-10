import weakref
# Test weakref.ref using objects of all builtin types

def check(name, func):
    obj = getattr(builtins, name)()
    r = func(obj)
    rr = r()
    assert obj is rr, (name, obj, rr)
    del obj
    assert r() is None, name

def test_normal():
    check('int', weakref.ref)
    check('str', weakref.ref)
    check('dict', weakref.ref)
    check('list', weakref.ref)
    check('tuple', weakref.ref)
    check('set', weakref.ref)
    check('object', weakref.ref)
    check('object', weakref.proxy)

def test_callable():
    # The types module checks that the object is callable.
    # We skip this test for old-style classes, because there isn't a
    # good way to define non-callable old-style classes.
    check('type', weakref.ref)
    check('type', weakref.proxy)

def test_kwargs():
