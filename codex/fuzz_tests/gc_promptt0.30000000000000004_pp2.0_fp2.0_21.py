import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs

class Test:
    pass

def callback(obj):
    print "callback called"

def test_callback():
    t = Test()
    w = weakref.ref(t, callback)
    del t
    gc.collect()
    print "callback not called yet"
    gc.collect()
    print "callback called"

def test_callback_with_args():
    t = Test()
    w = weakref.ref(t, callback, "arg")
    del t
    gc.collect()
    print "callback not called yet"
    gc.collect()
    print "callback called"

def test_callback_with_kwargs():
    t = Test()
    w = weakref.ref(t, callback, kwarg="arg")
    del t
    gc.collect()
    print "callback not called yet"
    gc.collect()
    print "callback called"

def test_callback_with_args_and_kwargs():
    t = Test()
    w = weakref.ref
