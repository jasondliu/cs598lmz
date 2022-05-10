import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class C:
    pass

def callback(x):
    print('collected', x)


c = C()
w = weakref.ref(c, callback)
c = None
gc.collect()  # call callback
w = None
gc.collect()  # don't call callback again
gc.collect()  # don't call callback again
gc.collect()  # don't call callback again
gc.collect()  # don't call callback again
gc.collect()  # don't call callback again
gc.collect()  # don't call callback again
gc.collect()  # don't call callback again
gc.collect()  # don't call callback again
gc.collect()  # don't call callback again
gc.collect()  # don't call callback again
gc.collect()  # don't call callback again
gc.collect()  # don't call callback again
gc.collect()  # don't call callback again
gc.collect()  # don't call callback again
gc.collect()  # don't call callback again
gc.collect()  # don't call callback again
gc.
