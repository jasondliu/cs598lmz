import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() and that it calls __del__ methods on the right objects.
# Also test gc.garbage, which is a list of objects which couldn't be
# cleaned because they were part of a reference cycle.
#
# This test is somewhat fragile because it depends on gc triggering at
# particular points.  XXX A better way to do this would be nice.

# Create a bunch of objects, record their ids, and create references to them
# in a cycle.  Returns the list of objects, and a weakref to one of them.
def create_objects(n):
    objects = [C() for i in range(n)]
    objects.append(objects)
    w = weakref.ref(objects[0])
    del objects
    return objects, w

class C(object):
    def __init__(self):
        self.id = id(self)
        self.state = 0
    def __del__(self):
        self.state = 1
    def __repr__(self):
        return "<C object at 0x%x>" % self.id

def test_gc
