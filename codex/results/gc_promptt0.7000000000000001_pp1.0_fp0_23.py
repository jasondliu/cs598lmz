import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakref.ref()
#
# Weakrefs are normally cleared before the finalizer is called, but
# there was a bug where they would not be cleared if they were part
# of a cycle of objects.
def wfunc(ref):
    print "wfunc called with", ref()

class A:
    def __init__(self):
        self.w = weakref.ref(self, wfunc)

# Create a cycle of objects with weakrefs in it.
a = A()

import gc
gc.collect()
del a
gc.collect()
