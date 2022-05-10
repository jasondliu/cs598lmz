import weakref
# Test weakref.ref() with a class
# The simplest kind of reference is a raw reference created with the
# weakref.ref() function.  These reference objects return the object being
# referenced when called, and otherwise act like the original object.
# 
# Raw references are not callable (though the object being referenced is).
# The isCallable() method should not be overridden in subclasses.
# 
# The following example creates a Class which returns the same value from
# __repr__() and __str__().  This is not a very realistic class, but it's
# simple enough to highlight the use of a weak reference.


class C:

    def __init__(self, arg):
        self.arg = arg

    def __repr__(self):
        return str(self)

    def __str__(self):
        return 'C(%r)' % self.arg


# Create a few references, and an object with a reference to one of them.

c1 = C(1)
c2 = C(2)
d = C(c1)

# Now make a weak reference to each
