import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect, it collects everything if it can.
gc.collect()

import sys, imp

def test_simplest_considerations():
    # test whether objects that did not have a callback, but
    # are now being tracked by a callback, are immediately
    # garbage-collected at the next collection.
    class A(object):
        pass
    a = A()
    wr = weakref.ref(a, lambda a=a:a)
    wr2 = weakref.ref(a, lambda a=a:a)
    assert wr() is a
    assert wr2() is a
    del a, wr, wr2
    gc.collect()
    return

def test_notification():
    class A(object):
        pass
    class B(object):
        pass
    a = A()
    b1 = B()
    b2 = B()
    callback_args = []
    def callback(arg):
        callback_args.append(arg)
        assert arg() is a
        assert wr() is None
        assert wr2() is None
    wr =
