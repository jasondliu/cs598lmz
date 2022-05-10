import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect and weakrefs
# we expect three decref and a collectable as we are about to exit..
weakref.ref(object())
gc.collect()
gui.quit()
gui.join()
