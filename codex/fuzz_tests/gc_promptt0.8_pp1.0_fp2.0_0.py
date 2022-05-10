import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() being called directly

class A:
    pass

w = weakref.ref(A())

def f():
    x = [A()]
    x.append(x)
    del x

for i in range(8):
    print("round", i)
    f()
    gc.collect()
    print("collectable:", gc.collect())

del w
gc.collect()

print("done")
