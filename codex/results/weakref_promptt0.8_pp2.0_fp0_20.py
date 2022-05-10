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

    def on_delete(self, *args):
        print 'deleting instance %s' % (self.value,)

    def __del__(self):
        print 'deleting object (reference count zero) %s' % (self.value,)

# The weak reference is broken if the object is deleted;
# if the object itself deletes its weak reference, a circular
# reference count may occur.
def test():
    obj1 = MyObj(1)
    obj2 = weakref.ref(obj1, obj1.on_delete)
