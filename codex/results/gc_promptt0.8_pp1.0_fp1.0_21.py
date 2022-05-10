import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() when someone is still holding a reference to the
# object but they are holding it via a weakref.

def f():
    l = []
    l2 = []
    d = {1: 1}
    # Create a cycle
    l.append(l)
    # Track this object, but don't create a cycle
    l2.append(d)
    w = weakref.ref(d)
    del l, l2
    return w

w = f()
gc.collect()
print w() is None
print gc.collect()    # prints 2
