import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
w = None
gc.collect()
del w
gc.collect()

# Test gc.callbacks
class Test_callbacks:
    def __init__(me, name):
        me.name = name
    def __del__(me):
        del me.name
        gc.collect()
        gc.collect()
        gc.collect()

    del Test_callbacks
    gc.collect()
    gc.collect()
    gc.collect()
    del gc.callbacks[:]

    def check(me):
        assert me.name == 'fred'
    def check_a(me, a):
        assert a == 5

    # Test gc.collect() callbacks
    l = []
    ref = weakref.ref(Test_callbacks('fred'), lambda a: l.append(a))
    gc.collect()
    assert l == [ref().name]
    del l[:]

    # Test gc.collect() callbacks with a parameter
    ref = weakref.ref(Test_callbacks('fred'), lambda
