import weakref
# Test weakref.ref
# Ensure that weakrefs to functions are properly handled
# by the weakref machinery

# The weakref machinery is responsible for creating/destroying
# weakref slots in the object's __weakref__ dict.

# The test is a regression test for the weakref machinery
# in type_set_item().  It uses the fact that the weakref machinery
# is not invoked when a __weakref__ slot is set to None.

# The test also tests the behavior of the weakref machinery
# when called with an object of a type that doesn't have a
# __weakref__ slot.  This is an edge case: it was previously
# handled incorrectly by the weakref machinery.

# Create a function (the object to be weakly referenced)
# which has a __del__ method.

def f():
    pass
f.__del__ = lambda : None


def test():
    r = weakref.ref(f)
    # create a weakref
    assert r() is f
    # check that the weakref works
    f.__weakref__ = None
    # set the __weakref
