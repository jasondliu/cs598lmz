import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref callback

class C:
    pass

callback_ran = False

def callback(wr):
    global callback_ran
    callback_ran = True

def test():
    c = C()
    wr = weakref.ref(c, callback)
    del c
    gc.collect()
    assert callback_ran

test()
