import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect with weakrefs.
#
# Create a bunch of objects, cyclic garbage and non-cyclic garbage.
# Create a bunch of weakrefs to the objects, some of which are callback
# weakrefs.  Verify that all the objects die, and that the callbacks are
# invoked.

import gc
import weakref
import sys

# Create a bunch of objects, and a callback that checks that an object
# is still alive.
objects = []
callbacks = weakref.WeakKeyDictionary()

class Callback:
    def __init__(self, obj):
        self.obj = obj
    def __call__(self, wr):
        if wr() is not self.obj:
            raise AssertionError("wrong object")

def callback(obj):
    callbacks[obj] = 1

for i in range(200):
    if i % 5 == 0:
        # create a cycle
        o = []
        objects.append(o)
        o.append(o)
    else:
        o = []
        objects.append(o)

   
