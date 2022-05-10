import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
# Create some dangling references.
d = []
def append(obj, weak=False):
    # We must keep a strong reference to the dict inserted in the list,
    # otherwise, when the list is resized, it will be removed and a dangling
    # reference will remain.
    d.append({})
    r = weakref.ref(obj, append)
    if weak:
        wr = r
    else:
        wr = weakref.ref(obj)
    try:
        del obj
    except NameError:
        # See below
        pass
    return wr, r

def create_objects(n):
    global x
    for i in range(n):
        x = C()
        wr, r = append(x)
    # Just return a basic object with a finalizer that deletes global x
    # (needed because otherwise "x" would only be deleted when "del x"
    # executes, and in that case gc() does not collect cycle).  This also
    # has the side effect of making x a zombie.
    # A bug in PyEval_
