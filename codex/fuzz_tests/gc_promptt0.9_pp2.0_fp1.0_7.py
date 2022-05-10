import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() does not improperly collect weakrefable objects
# when there are reachable weakrefs to them.  Also test that such weakrefs
# are not finalizers.
#
# test1() tests the first gc.collect(), when there may already be finalizers
# waiting to be called.  test2() tests subsequent gc.collect()s, when
# finalizers have already been invoked and the zombie queue is empty.
def test1(obj1, obj2, obj3):
    # Create a reference cycle.  Try to force obj1 to be collected, which
    # should fail since obj2 points to it.
    ref1 = weakref.ref(obj1)
    wref1 = weakref.ref(obj2)
    obj2.attr = obj1
    obj1.attr = obj2
    obj1.ref = ref1

    obj3 = None # Make sure obj3 is collectable
    obj3 = obj2
    wref2 = weakref.ref(obj2)
    assert wref2.__call__() is obj2
    assert wref1.__call__() is
