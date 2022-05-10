import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
# This will also test gc.garbage

def test_gc_collect():
    # Check that gc.garbage is empty
    if gc.garbage:
        raise TestFailed, "gc.garbage not empty at start"

    # Create a few objects
    class A:
        pass
    class B(object):
        pass
    a = A()
    b = B()
    a.b = b
    b.a = a
    del a, b

    # Check that gc.garbage is still empty
    if gc.garbage:
        raise TestFailed, "gc.garbage not empty after creating a few objects"

    # Create a few more objects
    for i in xrange(10):
        exec "a%d = A(); b%d = B()" % (i, i)
        exec "a%d.b = b%d; b%d.a = a%d" % (i, i, i, i)

    # Check that gc.garbage is still empty
    if gc.garbage:
