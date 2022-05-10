import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref callback.

import weakref

# Create a class with a __del__ method
class Foo:
    def __del__(self):
        print "Foo.__del__"

# Create a Foo instance
f = Foo()

# Create a weakref to f
r = weakref.ref(f, lambda x: print("weakref callback"))

# Delete f
del f

# Collect the garbage
gc.collect()
