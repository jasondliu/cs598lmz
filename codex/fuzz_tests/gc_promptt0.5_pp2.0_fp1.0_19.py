import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref callback.
#
# The callback should be called when the object is collected.
# The callback should not be called when the object is not collected.
# The callback should not be called more than once.
# The callback should be called at the very end of the collection.
# The callback should be called even if the object is involved in a cycle.

# We need a class with a destructor to make sure the callback is called
# at the very end of the collection.
class A:
    def __init__(self):
        self.destructor = self.destructor_called
    def destructor_called(self):
        self.destructor = self.destructor_called_again
    def destructor_called_again(self):
        print "destructor called twice!"

def callback(ref):
    print "callback called"
    if ref.destructor is not ref.destructor_called_again:
        print "callback called too early"

def check(obj):
    if obj.destructor is not obj.destructor_called_again:
        print "object not collected"
