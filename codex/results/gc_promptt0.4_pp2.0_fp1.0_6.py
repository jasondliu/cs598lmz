import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref callback that raises an exception.

def callback(wr):
    raise Exception("callback")

wr = weakref.ref(object(), callback)

for i in range(10):
    gc.collect()

print("OK")
