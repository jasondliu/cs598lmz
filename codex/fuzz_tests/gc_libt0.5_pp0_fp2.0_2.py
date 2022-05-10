import gc, weakref

def test_weakref_callbacks():
    # Test weakref callbacks
    #
    # This is a bit tricky, because we want to test that the callbacks
    # get called at the right time.  We create a data structure using
    # a list of weakrefs, where a callback will remove an item from the
    # list when it gets called.  To make sure all the callbacks get
    # called, we create a cycle with a list, and mutate the list while
    # we're in the middle of iterating over it.  The list is mutable
    # so that it's not eligible for immediate garbage collection.
    # Without the mutation, the cycle would get garbage collected
    # immediately.  With the mutation, the cycle gets broken when the
    # last weakref callback is invoked.
    #
    # Note that this test assumes that the callbacks are called
    # *immediately* when the weakrefs go away, and not during some
    # future garbage collection pass.  This assumption isn't part of
    # the weakref specification, but (as of Python 2.3) it
