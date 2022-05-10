import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collectable
def get_r():
        return gc.collectable()

def f():
    x = {}
    y = [1, 2]
    m = weakref.ref(y)

    y = 3.2

    return get_r

r = f()
L = [None]
for i in range(3):
    gc.collect()
    L.append(r())

assert L == [None, ([],), (['1', '2']), (['1', '2'],)]

print("gc: OK")
