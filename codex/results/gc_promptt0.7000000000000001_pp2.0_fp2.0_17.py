import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect
#
# This tests all the edge cases of gc.collect:
#
#   - weakref callbacks are called
def callback(wr):
    global seen
    assert len(seen) == 1
    seen.append(wr)

def callback2(wr):
    global seen
    assert len(seen) == 2
    assert wr is seen[1]
    seen.append(wr)

#   - finalizers are called
#   - finalizers call gc.collect
def finalize_test(obj):
    global finalizer_called
    try:
        finalizer_called.append(obj)
    except AttributeError:
        print("finalizer called")
        finalizer_called = [obj]

#   - weakrefs are updated
def update_weakref(wr):
    global updated_weakref
    assert updated_weakref is None
    updated_weakref = wr

#   - finalizers can resurrect objects
def finalize_resurrect():
    global finalizer_resurrected, finalizer_called, finalizer_resurrected

