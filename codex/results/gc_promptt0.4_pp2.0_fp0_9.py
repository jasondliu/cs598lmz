import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref callback.

# Create a callback that raises an exception.

class Boom(Exception): pass

def boom():
    raise Boom

# Create a callback that calls boom().

def boom_cb(x):
    boom()

# Create a callback that calls boom() when the object is collected.

def boom_when_collected(x):
    def boom_cb(x=x):
        boom()
    wr = weakref.ref(x, boom_cb)

# Create a callback that calls boom() when the object is finalized.

def boom_when_finalized(x):
    def boom_cb(x=x):
        boom()
    wr = weakref.ref(x, boom_cb)
    wr.finalize()

# Create a callback that calls boom() when the object is finalized
# and when the object is collected.

def boom_when_finalized_and_collected(x):
    def boom_cb(x=x):
        boom()
    wr = weakref.ref(x, boom_cb)
    wr
