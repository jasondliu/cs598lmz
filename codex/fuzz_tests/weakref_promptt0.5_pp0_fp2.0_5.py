import weakref
# Test weakref.ref(x)
#
# Usage:
#  import test.test_weakref
#  test.test_weakref.ref_test(MyClass)

def ref_test(C):
    import gc
    class MyClass:
        pass

    a = C()
    ra = weakref.ref(a)
    b = C()
    rb = weakref.ref(b)
    c = C()
    rc = weakref.ref(c)

    assert ra() is a
    assert rb() is b
    assert rc() is c

    del a
    gc.collect()
    assert ra() is None
    assert rb() is b
    assert rc() is c

    del b
    gc.collect()
    assert ra() is None
    assert rb() is None
    assert rc() is c

    del c
    gc.collect()
    assert ra() is None
    assert rb() is None
    assert rc() is None

# Test weakref.proxy(x)
#
# Usage:
#  import test.
