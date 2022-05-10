import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref whose callback has run.
# First time, no callback.
def callback(x):
    print "callback", x
    y = weakref.ref(x, callback)
l = []
for i in range(5):
    a = []
    a.append(a)
    l.append(weakref.ref(a, callback))
# Second time, with callback.
del l
gc.collect()
gc.set_debug(gc.DEBUG_UNCOLLECTABLE | gc.DEBUG_SAVEALL)
gc.collect()

# Test gc.collect() with a weakref whose callback has run.
# First time, no callback.
def callback(x):
    print "callback", x
    y = weakref.ref(x, callback)
l = []
for i in range(5):
    a = []
    a.append(a)
    l.append(weakref.ref(a, callback))
# Second time, with callback.
del l
gc.collect()
gc.set_debug(gc.DEBUG_UNCOLLECTABLE | g
