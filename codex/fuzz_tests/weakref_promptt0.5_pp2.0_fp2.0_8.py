import weakref
# Test weakref.ref() and weakref.proxy()

# This is a test of the weakref.ref() function.  The function is
# called with an object as the argument, and returns a weak reference
# object that acts as a transparent reference to the original object.
# The weak reference object is callable, and when called, returns the
# original object.  If the original object has been garbage collected,
# calling the weak reference object will cause None to be returned.

# This is a test of the weakref.proxy() function.  The function is
# called with an object as the argument, and returns a weak reference
# object that acts as a transparent proxy for the original object.
# The weak reference object is callable, and when called, calls the
# original object.  If the original object has been garbage collected,
# calling the weak reference object will raise a ReferenceError.

# This is a test of the weakref.getweakrefcount() function.  The
# function is called with an object as the argument, and returns the
# number of weak references to the object.

# This is a test of the weakref.getweakref
