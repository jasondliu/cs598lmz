import weakref
# Test weakref.ref(instance, on_delete) and __del__
#
# This isn't really a test, but a demonstration of how to use weakref.ref,
# and a basic test of the new implementation of weak references in
# Pyrex.

# the object is not deleted until its weak reference is deleted;
# here we create a strong reference to the weak reference, so the
# object doesn't get deleted by the garbage collector while we're
# not looking
class MyObj(object):
    def __init__(self, value):
        self.value = value

