import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a callback
def callback(x):
    print "callback", x

def f():
    callback(1)
    f = lambda: callback(2)
    wr = weakref.ref(f, callback)
    callback(3)
    del f
    gc.collect()
    print wr()
    callback(4)
    gc.collect()

f()

# Test gc.collect() with a finalizer
def finalizer(x):
    print "finalizer", x

def f():
    finalizer(1)
    f = lambda: finalizer(2)
    wr = weakref.ref(f, finalizer)
    finalizer(3)
    del f
    gc.collect()
    print wr()
    finalizer(4)
    gc.collect()

f()
