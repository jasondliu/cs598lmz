import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
if verbose:
    print("Testing gc.collect()...")

N = 5
class X(object):
    pass

wr = weakref.ref(X())

for i in range(N):
    gc.collect()
    lst = [X() for j in range(100)]
    for j in range(10):
        lst = lst + lst
    if wr() is not None:
        if verbose:
            print(" OK (object still alive)")
    else:
        raise TestFailed("gc didn't keep alive the existing weakref")
    gc.collect()

del lst
X = None

gc.collect()
if wr() is not None:
    raise TestFailed("gc didn't collect the existing weakref")
else:
    if verbose:
        print(" OK")

# Test weakref.ref()
if verbose:
    print("Testing weakref.ref()...")

def f():
    pass

wdr = weakref.ref(f)
gc.collect()
if w
