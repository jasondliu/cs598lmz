import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref
#
# This test will fail if the weakref is not cleared before the object is
# collected.

# Create a class with a __del__ method
class foo:
    def __del__(self):
        print "foo.__del__"

def callback(r):
    print "callback"

# Create a weak reference to the object
r = weakref.ref(foo(), callback)

# Collect the object
gc.collect()
