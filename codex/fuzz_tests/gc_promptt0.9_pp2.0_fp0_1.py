import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() in the recursive call chain of weakref callbacks
def callbacks(callback):
  callback(callback)
callbacks(lambda x: weakref.ref(x, lambda x: callbacks(x)))
a = {}; gc.collect()
