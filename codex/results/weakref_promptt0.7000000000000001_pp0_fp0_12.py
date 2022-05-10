import weakref
# Test weakref.ref(weakref.ref(foo))

def test_weakref_to_weakref(x):
    y = weakref.ref(x)
    z = weakref.ref(y)
    return z

class Foo(object):
    pass

for i in range(100):
    foo = Foo()
    gc.collect()
    z = test_weakref_to_weakref(foo)
    del foo
    gc.collect()
    try:
        z()
    except ReferenceError:
        # We expect that foo has been collected
        pass
    else:
        raise AssertionError("weakref to weakref is not working")
    del z
    gc.collect()

# Test weakref.ref(weakref.ref(weakref.ref(foo)))

def test_weakref_to_weakref_to_weakref(x):
    y = weakref.ref(x)
    z = weakref.ref(y)
    w = weakref.ref(z)
    return w

for i in range(100):

