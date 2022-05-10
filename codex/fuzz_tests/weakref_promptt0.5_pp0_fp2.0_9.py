import weakref
# Test weakref.ref() and weakref.proxy()

import weakref
import gc

class Foo:
    pass

def test(x):
    f = Foo()
    r = weakref.ref(f)
    p = weakref.proxy(f)
    assert r() is f
    assert p is f
    del f
    gc.collect()
    assert r() is None
    try:
        p.attr
    except ReferenceError:
        pass
    else:
        assert 0, "proxy should have died"

test(1)
test(2.0)
test(1+1j)
test('spam')
test(u'spam')
test((1,2,3))
test([1,2,3])
test({1:2, 3:4})

# Test weakref.KeyedRef()

class Foo:
    pass

def test(x):
    f = Foo()
    r = weakref.KeyedRef(f, lambda x: x)
    assert r() is f
    del f
    gc.collect()
