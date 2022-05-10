import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect().
print "running test_gc_collect..."
gc.collect()

# Test weakrefs.
print "running test_weakref..."
class C(object):
    pass
def callback(obj):
    callback.called = 1
callback.called = 0
def test(obj):
    w = weakref.ref(obj, callback)
    return w

# Case 1: the weakref is still alive and the object is too
c = C()
w = test(c)
gc.collect()
if callback.called:
    raise "callback should not have been called"
del c
gc.collect()
if callback.called:
    raise "callback should not have been called"
if w() is not None:
    raise "weakref should not have been called"

# Case 2: the weakref and the object die together
c = C()
w = test(c)
del c
gc.collect()
if not callback.called:
    raise "callback should have been called"

# Case 3: the weakref dies and the object lives
c = C()
w = test(
