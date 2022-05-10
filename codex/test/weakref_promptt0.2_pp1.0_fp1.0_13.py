import weakref
# Test weakref.ref() and weakref.proxy()

class Foo:
    pass

class Bar:
    pass

def test():
    f = Foo()
    b = Bar()
    r = weakref.ref(f)
    p = weakref.proxy(f)
    assert r() is f
    assert p is f
    assert r() is p
    assert weakref.getweakrefcount(f) == 1
    assert weakref.getweakrefs(f) == [r]
    del f
    gc.collect()
    assert r() is None
    try:
        p.x
    except ReferenceError:
        pass
    else:
        raise AssertionError
    try:
        r()
    except ReferenceError:
        pass
    else:
        raise AssertionError
    try:
        p.x
    except ReferenceError:
        pass
    else:
        raise AssertionError
    try:
        r()
    except ReferenceError:
        pass
    else:
        raise AssertionError
