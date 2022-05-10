import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect crashes due to weakref created while request-held by
# subTest's __exit__.
def test_gtc_collect_crash():
    gc.collect()
    with unittest.subTest():
        w = weakref.ref(object)
        del w, unittest.subTest
    gc.collect()
