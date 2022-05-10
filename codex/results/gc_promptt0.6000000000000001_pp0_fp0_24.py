import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs.

class C(object):
    pass

def func():
    a = C()
    wr = weakref.ref(a)
    del a
    gc.collect()
    if wr() is not None:
        print "not collected"

func()

# Another test: if the weakref is kept alive, the object will not be collected.

class C(object):
    pass

def func():
    a = C()
    wr = weakref.ref(a)
    del a
    gc.collect()
    if wr() is not None:
        print "not collected"
    else:
        print "collected"

func()

# Now, if the weakref is not kept alive, the object will be collected.

class C(object):
    pass

def func():
    a = C()
    wr = weakref.ref(a)
    del a
    gc.collect()
    if wr() is not None:
        print "not collected"
    else:
        print "collected"

