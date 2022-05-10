import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect with a weakref callback that is called during
# collection.  The callback should be called before the object is
# finalized.

class A:
    pass

class B:
    pass

def callback(wr):
    print "callback"
    a = wr()
    assert a.b is None
    assert a.finalized
    assert not a.finalizing
    a.finalizing = 1

a = A()
a.b = B()
a.finalized = 0
a.finalizing = 0
wr = weakref.ref(a, callback)

gc.collect()
assert a.finalized
assert a.finalizing

# Test the same thing with a callback that raises an exception.
class A:
    pass

def callback(wr):
    print "callback"
    a = wr()
    assert a.finalized
    assert not a.finalizing
    a.finalizing = 1
    raise ValueError

a = A()
a.finalized = 0
a.finalizing = 0
wr = weakref.ref(a, callback)

try:
