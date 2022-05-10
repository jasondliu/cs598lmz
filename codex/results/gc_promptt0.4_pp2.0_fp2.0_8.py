import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs

class A:
    pass

def callback(ref):
    print "callback", ref

def test():
    # Create a cycle, and a weakref to one of the objects in the cycle.
    a = A()
    a.b = A()
    a.b.a = a
    a.b.b = a.b
    a.b.c = weakref.ref(a, callback)

    # Break the cycle.
    a.b = None
    del a

    # Collecting now won't find the cycle, and the weakref callback
    # won't be called.
    gc.collect()

    # Now create a new cycle, and a weakref to one of the objects in
    # the cycle.
    a = A()
    a.b = A()
    a.b.a = a
    a.b.b = a.b
    a.b.c = weakref.ref(a, callback)

    # Break the cycle, and collect again.  This time the weakref
    # callback will be called.

