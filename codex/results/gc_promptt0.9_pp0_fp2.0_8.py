import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() to ensure finalizers are executed

# Keep a list of objects which we expect to find during collection, before
# finalizers are run.  Note that there's no guarantee about the order in which
# objects with finalizers will be finalized, but the object's finalizer should
# remove the object from this list after finalization.
reachable_objects = []

# Check if Python is built with COUNT_ALLOCS.
cannot_collect = not hasattr(sys, 'getcounts')

def test2(x, y=[], testfunc=None, version=[],
          append=reachable_objects.append):
    #
    # If a function defines a local variable with the same name as a global
    # variable, you don't get the global one.  This can bite if you define a
    # default argument equal to some global mutable; future calls will keep
    # adding to the same list, and future default argument evaluations will
    # see the everlasting effects of earlier calls.  This check ensures we
    # understand that problem. :-)
    #
    # Note that "y is not reachable_objects"
