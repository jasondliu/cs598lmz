import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() and gc.garbage.
def test(collect):
    print 'collecting',
    if collect:
        print 'immediately',
        gc.collect()
    else:
        print 'later',
    print '-'*20
    print 'creating cycles...',
    # Create a cycle.
    l = [{}]
    d = {'a':l}
    l.append(d)
    w = weakref.ref(d)
    # Enter the cycle.
    l = d = w()
    # Check that everything is ok.
    print 'before, d=', d
    assert d is not None
    # Delete everything.
    del l, d
    # Check that the objects have been freed.
    print 'after, d=', w()
    assert w() is None
    # Check that gc.garbage contains the objects.
    print 'garbage:', gc.garbage
    assert gc.garbage
    gc.garbage[:] = []

print 'testing immediate collection'
test(1)
print 'testing
