import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() called before weakref callback
# is invoked.
def callback(wr):
    print 'callback called'
    assert wr() is None

l = []
l.append(l)
l.append(l)
l.append(l)
print 'creating weakref'
wr = weakref.ref(l, callback)
print 'collected'
gc.collect()
print 'done'
