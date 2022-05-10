import weakref
# Test weakref.ref() with callbacks

# This is a test of the callback feature of weakref.ref().

# The callback is called with the weak reference object as its
# only argument.

# A weakref is created with a reference to an object.  When the
# object is about to be destroyed, the weak reference is notified
# by having its callback function called.  The callback function
# must be able to deal with the weak reference object being a
# dead reference.

# The weak reference object is callable and returns the referenced
# object or None if the referenced object no longer exists.

# A weak reference can be used to break a reference cycle.

# This test creates a reference cycle and verifies that the
# objects in the cycle are eventually deleted.  It also checks
# that callback functions are called before the referenced
# objects are destroyed.

# This test is also used to verify that the __del__ method of
# a weak reference is not called when the weak reference
# object is still alive and the referenced object is still
# alive.

# Note that this test does not verify that the objects in a
# reference cycle are
