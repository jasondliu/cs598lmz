import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() right after creating a weakref.

class C:
    pass

c = C()

def callback(w):
    print("callback", w)

w = weakref.ref(c, callback)

print("collecting...")
gc.collect()
print("done")

del c

print("collecting...")
gc.collect()
print("done")
