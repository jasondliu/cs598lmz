import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakref objects.

def create_objects(l):
    for i in range(0, 100):
        o = [i]
        o.append(o)
        l.append(weakref.ref(o))
    return l

def create_objects_with_callback(l):
    def callback(w):
        callback.counter += 1

    callback.counter = 0
    for i in range(0, 100):
        o = [i]
        o.append(o)
        l.append(weakref.ref(o, callback))
    return callback.counter

def test(n):
    # Create some objects.
    l = []
    create_objects(l)
    del l

    # Collect the objects.
    gc.collect()

    # Collect the objects.  This should not trigger any callbacks.
    gc.collect()

    # Create some objects.
    l = []
    create_objects_with_callback(l)
    del l

    # Collect the objects.
    count = gc.collect()

    # Collect
