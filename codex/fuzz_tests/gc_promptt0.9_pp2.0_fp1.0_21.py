import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() after removing a weakref from gc.garbage.
# Weakref callbacks did not run when the weakref was removed from
# gc.garbage, so __del__ methods were not called and objects with
# __del__ methods were not collectable.
# See issue #1856.

def callback(o):
    if o is not None:
        print('callback called with', repr(o))
        l.append(o)

l = []
d = {}
wr = weakref.ref(d, callback)
d_wr = weakref.ref(d)
d_wr_id = id(d_wr)

def foo():
    gc.collect()
    assert len(l) == 1 and l[0] is d
    assert d_wr is None

# foo() and its locally reference d are not collectable unless we put
# d_wr into gc.garbage, because d and d_wr are mutually reachable
# through the callback.
gc.garbage.append(d_wr)
foo()
gc.garbage.pop()

#
