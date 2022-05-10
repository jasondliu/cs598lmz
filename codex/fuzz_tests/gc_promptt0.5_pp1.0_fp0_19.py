import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
def test_collect():
    # Test the effect of collect() on various types of objects.
    #
    # Test that collect() doesn't collect objects which are still
    # reachable.
    #
    # Test that collect() does collect objects which are no longer
    # reachable.
    #
    # Test that collect() invokes finalizers on objects which are no
    # longer reachable.
    #
    # Test that collect() invokes finalizers on objects which are
    # reachable only by finalizers of other objects.
    #
    # Test that collect() invokes finalizers on objects which are
    # reachable only by finalizers of other objects, even if the
    # objects are reachable by other means.
    #
    # Test that collect() does not invoke finalizers on objects which
    # are still reachable.
    #
    # Test that collect() does not invoke finalizers on objects which
    # are reachable only by finalizers of other objects, if the
    # objects are still reachable by other means.
    #
    # Test that collect() invokes final
