import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect recursive (issue #11018).

def test():
    def f():
        def g():
            do_collect = weakref.ref(g)
            g()
        g()
    f()

test()
