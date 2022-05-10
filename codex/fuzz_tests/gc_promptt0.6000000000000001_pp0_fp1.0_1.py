import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref
class C:
    pass
c = C()
def callback(w):
    print("callback: ", w)
w = weakref.ref(c, callback)
print("callback: ", w)
del c
gc.collect()
print("callback: ", w)
print("callback: ", w)
print("callback: ", w)
print("callback: ", w)
print("callback: ", w)
