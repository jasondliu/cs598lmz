import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() and gc.garbage.
garbage = []

def n():
    n = 1
    while n < 500:
        yield n
        n += 1

def untrack(obj):
    # untrack the object from the garbage collector
    for i, item in enumerate(gc.garbage):
        if isinstance(item, weakref.ReferenceType):
            if item() == obj:
                gc.garbage[i] = None
# test gc.get_objects
def objs_of_type(t):
    gc.collect()
    objects = gc.get_objects()
    return [ obj for obj in objects if isinstance(obj, t) ]

def q(v):
    return ref(v) in objs_of_type(ref)

def x(v):
    return ref(v) in gc.garbage

def l():
    l = range(5)
    print len(l)
    return l

def dis(l, i):
    del l[i:]

class obj:
    pass
