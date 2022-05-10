import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect after a weakref callback has removed the last
# reference to an object.

# The bug was that the finalizer would be executed while the object was
# still being tracked as collectable.  (The finalizer would also be
# executed twice in this case.)

class C:
    def __del__(self):
        print "deleted"

class D:
    def __init__(self, obj):
        self.wr = weakref.ref(obj, self.callback)

    def callback(self, ref):
        print "callback"

def make():
    o = C()
    d = D(o)
    # Clear the reference to o, and make it unreachable
    o = None
    d = None

make()
gc.collect()
