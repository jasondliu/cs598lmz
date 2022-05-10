import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() and weakref.ref()
#
# Create a cycle with a function object and a frame object
# The function object holds a reference to the frame object.
# The frame object holds a reference to the function object.
#
# The weakref.ref() call should break the cycle, allowing the
# function object to be collected.  The frame object should
# be left behind.

import gc, weakref

def f():
    return f

def test_weakref_with_frame(debug=gc.DEBUG_STATS):
    gc.set_debug(debug)
    f().f_locals
    r = weakref.ref(f)
    gc.collect()
    assert r() is None
    gc.set_debug(0)

def test_weakref_with_frame_and_dict(debug=gc.DEBUG_STATS):
    gc.set_debug(debug)
    d = {}
    def g():
        return d
    g().f_locals
    r = weakref.ref(g)
    gc.collect()

